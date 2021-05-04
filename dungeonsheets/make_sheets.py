#!/usr/bin/env python

import logging
import argparse
import os
import subprocess
import warnings
import re
from pathlib import Path
from multiprocessing import Pool, cpu_count
from itertools import product

from jinja2 import Environment, PackageLoader

from dungeonsheets import character as _char
from dungeonsheets import exceptions, readers, latex
from dungeonsheets.stats import mod_str
from dungeonsheets.fill_pdf_template import (
    create_character_pdf_template,
    create_spells_pdf_template,
)
from dungeonsheets.character import Character

PDFTK_CMD = "pdftk"

log = logging.getLogger(__name__)

ORDINALS = {
    1: "1st",
    2: "2nd", 
    3: "3rd", 
    4: "4th", 
    5: "5th", 
    6: "6th", 
    7: "7th", 
    8: "8th",
    9: "9th"
}

"""Program to take character definitions and build a PDF of the
character sheet."""

bold_re = re.compile(r"\*\*([^*]+)\*\*")
it_re = re.compile(r"\*([^*]+)\*")
verb_re = re.compile(r"``([^`]+)``")
heading_re = re.compile(r"^[ \t\r\f\v]*(.+)\n\s*([-=\^]+)$", flags=re.MULTILINE)
# What defines a list in reST:
# - a blank line
# - one or more of the following
#   - "- [a-z]"
#   - an additional line of text (if multi-line bullets)
#   - a blank line
# - a blank line
# - a non-list line or end of file
# list_re = re.compile('^[ \t\r\f\v]*\n((?:\s*[-*+]\s+[^\n]*\n)+)', flags=re.MULTILINE)
list_re = re.compile(
    r"^[ \t\r\f\v]*\n"  # A blank line
    r"((?:\s*[-*+]\s+[^\n]*\n)+)"  # The first line of each list item
    "",
    flags=re.MULTILINE,
)
# What defines a list item in reST:
# - a line starting with "- " then some text
# - zero or more lines starting with anything other than "- "
list_item_re = re.compile(r"^\s*[-*+]\s+", flags=re.MULTILINE)


def _parse_rst_lists(rst):
    """Read lists in reST and iterate.

    Yields
    ======
    list_rst : str
      The matching reST list found in the input text
    list_items : list
      A python list of the items found in the reST list.

    """
    for match in list_re.finditer(rst):
        list_rst = match.group(0)
        # Separate the list items
        list_items = list_item_re.split(match.group(1))
        # Clean up separated list items
        list_items = list_items[1:]  # First item is an empty string
        list_items = [item.replace("\n", " ").strip() for item in list_items]
        yield list_rst, list_items


def _parse_rst_headings(rst):
    """Read headings in reST and iterate.

    Yields
    ======
    heading_rst : str
      The matching reST heading found in the input text.
    heading : str
      The text of the heading with underlining removed.
    level : int
      How deep the heading is: 0 is top-level, 1 is next level down,
      etc.

    """
    heading_levels = {
        "=": 0,
        "-": 1,
        "^": 2,
    }
    for match in heading_re.finditer(rst):
        heading_rst = match.group(0)
        heading, underline = match.groups()
        # Check for valid heading
        if len(underline) < len(heading):
            log.debug("Skipping malformed reST heading: '%s\n%s'", heading, underline)
            continue
        if len(set(underline)) > 1:
            log.debug("Skipping malformed reST heading: '%s\n%s'", heading, underline)
            continue
        # Valid heading, so determine how many levels deep it is
        level = heading_levels[underline[0]]
        yield heading_rst, heading, level


jinja_env = Environment(
    loader=PackageLoader("dungeonsheets", "forms"),
    block_start_string="[%",
    block_end_string="%]",
    variable_start_string="[[",
    variable_end_string="]]",
)
jinja_env.filters["rst_to_latex"] = latex.rst_to_latex
jinja_env.filters["mod_str"] = mod_str


PDFTK_CMD = "pdftk"


def create_druid_shapes_tex(
    character: Character,
    use_dnd_decorations: bool = False,
) -> str:
    template = jinja_env.get_template("druid_shapes_template.tex")
    return template.render(character=character, use_dnd_decorations=use_dnd_decorations)



def create_infusions_tex(
    character: Character,
    use_dnd_decorations: bool = False,
) -> str:
    template = jinja_env.get_template("infusions_template.tex")
    return template.render(character=character, use_dnd_decorations=use_dnd_decorations)


def create_spellbook_tex(
    character: Character,
    use_dnd_decorations: bool = False,
) -> str:
    template = jinja_env.get_template("spellbook_template.tex")
    return template.render(character=character, ordinals=ORDINALS, use_dnd_decorations=use_dnd_decorations)


def create_features_tex(
    character: Character,
    use_dnd_decorations: bool = False,
) -> str:
    template = jinja_env.get_template("features_template.tex")
    return template.render(character=character, use_dnd_decorations=use_dnd_decorations)


def make_sheet(
    character_file,
    character=None,
    flatten=False,
    latex_template=True,
    fancy_decorations=False,
    debug=False,
):
    """Prepare a PDF character sheet from the given character file.

    Parameters
    ----------
    character_file : str
      File (.py) to load character from. Will save PDF using same name
    character : Character, optional
      If provided, will not load from the character file, just use
      file for PDF name
    flatten : bool, optional
      If true, the resulting PDF will look better and won't be
      fillable form.
    fancy_decorations : bool, optional
      Use fancy page layout and decorations for extra sheets, namely
      the dnd style file: https://github.com/rpgtex/DND-5e-LaTeX-Template.
    debug : bool, optional
      Provide extra info and preserve temporary files.

    """
    if character is None:
        character = _char.Character.load(character_file)

    # Set the fields in the FDF
    char_base = os.path.splitext(character_file)[0] + "_char"
    sheets = [char_base + ".pdf"]
    pages = []
    tex = [jinja_env.get_template("preamble.tex").render(use_dnd_decorations=fancy_decorations)]

    # Start of PDF gen
    char_pdf = create_character_pdf_template(
        character=character, basename=char_base, flatten=flatten
    )
    pages.append(char_pdf)
    if character.is_spellcaster:
        # Create spell sheet
        spell_base = "{:s}_spells".format(os.path.splitext(character_file)[0])
        create_spells_pdf_template(
            character=character, basename=spell_base, flatten=flatten
        )
        sheets.append(spell_base + ".pdf")
    # end of PDF gen
    
    if character.is_spellcaster:
        tex.append(create_spellbook_tex(character, use_dnd_decorations=fancy_decorations))

    if len(character.spells) > 0:
        tex.append(create_spellbook_tex(character, use_dnd_decorations=fancy_decorations))
    # Create a list of Artificer infusions
    infusions = getattr(character, "infusions", [])
    if len(infusions) > 0:
        tex.append(create_infusions_tex(character, use_dnd_decorations=fancy_decorations))
    # Create a list of Druid wild_shapes
    wild_shapes = getattr(character, "wild_shapes", [])
    if len(wild_shapes) > 0:
        tex.append(create_druid_shapes_tex(character, use_dnd_decorations=fancy_decorations))


    tex.append(jinja_env.get_template("postamble.tex").render(use_dnd_decorations=fancy_decorations))
    latex.create_latex_pdf("".join(tex), "name", keep_temp_files=debug)
    if len(tex) > 2:
        sheets.append("name.pdf")
    # Typeset combined LaTeX file
    
    """
        shapes_base = os.path.splitext(character_file)[0] + "_wild_shapes"
        try:
            create_druid_shapes_pdf(
                character=character,
                basename=shapes_base,
                keep_temp_files=debug,
                use_dnd_decorations=fancy_decorations,
            )
        except exceptions.LatexNotFoundError:
            log.warning(
                "``pdflatex`` not available. Skipping wild shapes list "
                f"for {character.name}"
            )
        else:
            sheets.append(shapes_base + ".pdf")
        """
    # Combine sheets into final pdf
    final_pdf = os.path.splitext(character_file)[0] + ".pdf"
    merge_pdfs(sheets, final_pdf, clean_up=True)


def merge_pdfs(src_filenames, dest_filename, clean_up=False):
    """Merge several PDF files into a single final file.

    src_filenames
      Iterable of source PDF file paths to use.
    dest_filename
      Path to requested PDF filename, will be overwritten if it
      exists.
    clean_up : optional
      If truthy, the ``src_filenames`` will be deleted once the
      ``dest_filename`` has been created.

    """
    popenargs = (PDFTK_CMD, *src_filenames, "cat", "output", dest_filename)
    try:
        subprocess.call(popenargs)
    except FileNotFoundError:
        warnings.warn(
            f"Could not run `{PDFTK_CMD}`; skipping file concatenation.", RuntimeWarning
        )
    else:
        # Remove temporary files
        if clean_up:
            for sheet in src_filenames:
                os.remove(sheet)


load_character_file = readers.read_character_file


def _build(filename, args) -> int:
    basename = filename.stem
    print(f"Processing {basename}...")
    try:
        make_sheet(
            character_file=filename,
            flatten=(not args.editable),
            debug=args.debug,
            fancy_decorations=args.fancy_decorations,
        )
    except exceptions.CharacterFileFormatError:
        # Only raise the failed exception if this file is explicitly given
        print(f"invalid {basename}")
        if args.filename:
            raise
    except Exception:
        print(f"{basename} failed")
        raise
    else:
        print(f"{basename} done")
    return 1


def main():
    # Prepare an argument parser
    parser = argparse.ArgumentParser(
        description="Prepare Dungeons and Dragons character sheets as PDFs"
    )
    parser.add_argument(
        "filename",
        type=str,
        nargs="*",
        help="File with character definition, or directory containing such files",
    )
    parser.add_argument(
        "--editable",
        "-e",
        action="store_true",
        help="Keep the PDF fields in place once processed",
    )
    parser.add_argument(
        "--recursive",
        "-r",
        action="store_true",
        help="Descend into subfolders looking for character files",
    )
    parser.add_argument(
        "--fancy-decorations",
        "--fancy",
        "-F",
        action="store_true",
        help=(
            "Render extra pages using fancy decorations "
            "(experimental, requires https://github.com/rpgtex/DND-5e-LaTeX-Template)"
        ),
    )
    parser.add_argument(
        "--debug",
        "-d",
        action="store_true",
        help="Provide verbose logging for debugging purposes.",
    )
    args = parser.parse_args()
    # Prepare logging if necessary
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    # Build the true list of filenames
    input_filenames = args.filename
    known_extensions = readers.readers_by_extension.keys()
    if input_filenames == []:
        input_filenames = [Path()]
    else:
        input_filenames = [Path(f) for f in input_filenames]

    def get_char_files(fpath, parse_dirs=False):
        valid_files = []
        if fpath.is_dir() and parse_dirs:
            for f in fpath.iterdir():
                valid_files.extend(get_char_files(f, parse_dirs=args.recursive))
        elif fpath.suffix in known_extensions:
            valid_files.append(fpath)
        return valid_files

    temp_filenames = []
    for fpath in input_filenames:
        temp_filenames.extend(get_char_files(fpath, parse_dirs=True))
    # IMPORANT:
    # Check that the files are valid dungeonsheets files without importing them
    filenames = []
    version_re = re.compile(
        r"^dungeonsheets_version = [\'\"](?P<version>[0-9.]+)[\'\"]\s*$", re.MULTILINE
    )
    for fpath in temp_filenames:
        with open(fpath, mode="r") as fp:
            if version_re.search(fp.read()) or fpath.suffix != ".py":
                filenames.append(fpath)
    # Process the requested files
    if args.debug:
        for filename in filenames:
            _build(filename, args)
    else:
        with Pool(cpu_count()) as p:
            p.starmap(_build, product(filenames, [args]))


if __name__ == "__main__":
    main()
