"""
A collection of monsters from D&D 5e's SRD

This file was autogenerated by https://github.com/stravajiaxen/5e-srd-to-py
"""

from dungeonsheets.monsters.monsters import Monster
from dungeonsheets.stats import Ability


class Baboon(Monster):
    """

    Pack Tactics.
      The baboon has advantage on an attack roll against a creature if at
      least one of the baboon's allies is within 5 ft. of the creature and
      the ally isn't incapacitated.

    # Actions

    Bite.
      Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 1 (1d4 -
      1) piercing damage.
    """
    name = 'Baboon'
    description = 'Small beast, unaligned'
    challenge_rating = 0
    armor_class = 12
    skills = ''
    senses = 'Passive Perception 11'
    languages = ''
    strength = Ability(8)
    dexterity = Ability(14)
    constitution = Ability(11)
    intelligence = Ability(4)
    wisdom = Ability(12)
    charisma = Ability(6)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 30
    burrow_speed = 0
    hp_max = 3
    hit_dice = '1d6 + 0'
    condition_immunities = ''
    damage_immunities = ''
    damage_resistances = ''
    damage_vulnerabilities = ''
    spells = []


class Badger(Monster):
    """

    Keen Smell.
      The badger has advantage on Wisdom (Perception) checks that rely on
      smell.

    # Actions

    Bite.
      Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 1
      piercing damage.
    """
    name = 'Badger'
    description = 'Tiny beast, unaligned'
    challenge_rating = 0
    armor_class = 10
    skills = ''
    senses = 'Darkvision 30 ft., Passive Perception 11'
    languages = ''
    strength = Ability(4)
    dexterity = Ability(11)
    constitution = Ability(12)
    intelligence = Ability(2)
    wisdom = Ability(12)
    charisma = Ability(5)
    speed = 20
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    burrow_speed = 5
    hp_max = 3
    hit_dice = '1d4 + 1'
    condition_immunities = ''
    damage_immunities = ''
    damage_resistances = ''
    damage_vulnerabilities = ''
    spells = []


class Balor(Monster):
    """

    Death Throes.
      When the balor dies, it explodes, and each creature within 30 feet of
      it must make a DC 20 Dexterity saving throw, taking 70 (20d6) fire
      damage on a failed save, or half as much damage on a successful one.
      The explosion ignites flammable objects in that area that aren't being
      worn or carried, and it destroys the balor's weapons.
    Fire Aura.
      At the start of each of the balor's turns, each creature within 5 feet
      of it takes 10 (3d6) fire damage, and flammable objects in the aura
      that aren't being worn or carried ignite. A creature that touches the
      balor or hits it with a melee attack while within 5 feet of it takes
      10 (3d6) fire damage.
    Magic Resistance.
      The balor has advantage on saving throws against spells and other
      magical effects.
    Magic Weapons.
      The balor's weapon attacks are magical.

    # Actions

    Multiattack.
      The balor makes two attacks: one with its longsword and one with its
      whip.
    Longsword.
      Melee Weapon Attack: +14 to hit, reach 10 ft., one target. Hit: 21
      (3d8 + 8) slashing damage plus 13 (3d8) lightning damage. If the balor
      scores a critical hit, it rolls damage dice three times, instead of
      twice.
    Whip.
      Melee Weapon Attack: +14 to hit, reach 30 ft., one target. Hit: 15
      (2d6 + 8) slashing damage plus 10 (3d6) fire damage, and the target
      must succeed on a DC 20 Strength saving throw or be pulled up to 25
      feet toward the balor.
    Teleport.
      The balor magically teleports, along with any equipment it is wearing
      or carrying, up to 120 feet to an unoccupied space it can see.
    Variant: Summon Demon.
      The demon chooses what to summon and attempts a magical summoning.
      
      A balor has a 50 percent chance of summoning 1d8 vrocks, 1d6 hezrous,
      1d4 glabrezus, 1d3 nalfeshnees, 1d2 mariliths, or one goristro.
      
      A summoned demon appears in an unoccupied space within 60 feet of its
      summoner, acts as an ally of its summoner, and can't summon other
      demons. It remains for 1 minute, until it or its summoner dies, or
      until its summoner dismisses it as an action.
    """
    name = 'Balor'
    description = 'Huge fiend, chaotic evil'
    challenge_rating = 19
    armor_class = 19
    skills = ''
    senses = 'Truesight 120 ft., Passive Perception 13'
    languages = 'Abyssal, telepathy 120 ft.'
    strength = Ability(26)
    dexterity = Ability(15)
    constitution = Ability(22)
    intelligence = Ability(20)
    wisdom = Ability(16)
    charisma = Ability(22)
    speed = 40
    swim_speed = 0
    fly_speed = 80
    climb_speed = 0
    burrow_speed = 0
    hp_max = 262
    hit_dice = '21d12 + 126'
    condition_immunities = 'poisoned'
    damage_immunities = 'fire, poison'
    damage_resistances = 'cold'
    damage_vulnerabilities = ''
    spells = []


class Bandit(Monster):
    """

    # Actions

    Scimitar.
      Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 +
      1) slashing damage.
    Light Crossbow.
      Ranged Weapon Attack: +3 to hit, range 80 ft./320 ft., one target.
      Hit: 5 (1d8 + 1) piercing damage.
    """
    name = 'Bandit'
    description = 'Medium humanoid, any non-lawful alignment'
    challenge_rating = 0.125
    armor_class = 12
    skills = ''
    senses = 'Passive Perception 10'
    languages = 'any one language (usually Common)'
    strength = Ability(11)
    dexterity = Ability(12)
    constitution = Ability(12)
    intelligence = Ability(10)
    wisdom = Ability(10)
    charisma = Ability(10)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    burrow_speed = 0
    hp_max = 11
    hit_dice = '2d8 + 2'
    condition_immunities = ''
    damage_immunities = ''
    damage_resistances = ''
    damage_vulnerabilities = ''
    spells = []


class BanditCaptain(Monster):
    """

    # Actions

    Multiattack.
      The captain makes three melee attacks: two with its scimitar and one
      with its dagger. Or the captain makes two ranged attacks with its
      daggers.
    Scimitar.
      Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 +
      3) slashing damage.
    Dagger.
      Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60
      ft., one target. Hit: 5 (1d4 + 3) piercing damage.

    # Reactions

    Parry.
      The captain adds 2 to its AC against one melee attack that would hit
      it. To do so, the captain must see the attacker and be wielding a
      melee weapon.
    """
    name = 'Bandit Captain'
    description = 'Medium humanoid, any non-lawful alignment'
    challenge_rating = 2
    armor_class = 15
    skills = 'Athletics +4, Deception +4'
    senses = 'Passive Perception 10'
    languages = 'any two languages'
    strength = Ability(15)
    dexterity = Ability(16)
    constitution = Ability(14)
    intelligence = Ability(14)
    wisdom = Ability(11)
    charisma = Ability(14)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    burrow_speed = 0
    hp_max = 65
    hit_dice = '10d8 + 20'
    condition_immunities = ''
    damage_immunities = ''
    damage_resistances = ''
    damage_vulnerabilities = ''
    spells = []


class BarbedDevil(Monster):
    """

    Barbed Hide.
      At the start of each of its turns, the barbed devil deals 5 (1d10)
      piercing damage to any creature grappling it.
    Devil's Sight.
      Magical darkness doesn't impede the devil's darkvision.
    Magic Resistance.
      The devil has advantage on saving throws against spells and other
      magical effects.

    # Actions

    Multiattack.
      The devil makes three melee attacks: one with its tail and two with
      its claws. Alternatively, it can use Hurl Flame twice.
    Claw.
      Melee Weapon Attack: +6 to hit, reach 5 ft ., one target. Hit: 6 (1d6
      + 3) piercing damage.
    Tail.
      Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10 (2d6
      + 3) piercing damage.
    Hurl Flame.
      Ranged Spell Attack: +5 to hit, range 150 ft., one target. Hit: 10
      (3d6) fire damage. If the target is a flammable object that isn't
      being worn or carried, it also catches fire.
    """
    name = 'Barbed Devil'
    description = 'Medium fiend, lawful evil'
    challenge_rating = 5
    armor_class = 15
    skills = 'Deception +5, Insight +5, Perception +8'
    senses = 'Darkvision 120 ft., Passive Perception 18'
    languages = 'Infernal, telepathy 120 ft.'
    strength = Ability(16)
    dexterity = Ability(17)
    constitution = Ability(18)
    intelligence = Ability(12)
    wisdom = Ability(14)
    charisma = Ability(14)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    burrow_speed = 0
    hp_max = 110
    hit_dice = '13d8 + 52'
    condition_immunities = 'poisoned'
    damage_immunities = 'fire, poison'
    damage_resistances = 'cold'
    damage_vulnerabilities = ''
    spells = []


class Basilisk(Monster):
    """

    Petrifying Gaze.
      If a creature starts its turn within 30 ft. of the basilisk and the
      two of them can see each other, the basilisk can force the creature to
      make a DC 12 Constitution saving throw if the basilisk isn't
      incapacitated. On a failed save, the creature magically begins to turn
      to stone and is restrained. It must repeat the saving throw at the end
      of its next turn. On a success, the effect ends. On a failure, the
      creature is petrified until freed by the greater restoration spell or
      other magic.
      
      A creature that isn't surprised can avert its eyes to avoid the saving
      throw at the start of its turn. If it does so, it can't see the
      basilisk until the start of its next turn, when it can avert its eyes
      again. If it looks at the basilisk in the meantime, it must
      immediately make the save.
      
      If the basilisk sees its reflection within 30 ft. of it in bright
      light, it mistakes itself for a rival and targets itself with its
      gaze.

    # Actions

    Bite.
      Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6
      + 3) piercing damage plus 7 (2d6) poison damage.
    """
    name = 'Basilisk'
    description = 'Medium monstrosity, unaligned'
    challenge_rating = 3
    armor_class = 12
    skills = ''
    senses = 'Darkvision 60 ft., Passive Perception 9'
    languages = ''
    strength = Ability(16)
    dexterity = Ability(8)
    constitution = Ability(15)
    intelligence = Ability(2)
    wisdom = Ability(8)
    charisma = Ability(7)
    speed = 20
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    burrow_speed = 0
    hp_max = 52
    hit_dice = '8d8 + 16'
    condition_immunities = ''
    damage_immunities = ''
    damage_resistances = ''
    damage_vulnerabilities = ''
    spells = []


class Bat(Monster):
    """

    Echolocation.
      The bat can't use its blindsight while deafened.
    Keen Hearing.
      The bat has advantage on Wisdom (Perception) checks that rely on
      hearing.

    # Actions

    Bite.
      Melee Weapon Attack: +0 to hit, reach 5 ft., one creature. Hit: 1
      piercing damage.
    """
    name = 'Bat'
    description = 'Tiny beast, unaligned'
    challenge_rating = 0
    armor_class = 12
    skills = ''
    senses = 'Blindsight 60 ft., Passive Perception 11'
    languages = ''
    strength = Ability(2)
    dexterity = Ability(15)
    constitution = Ability(8)
    intelligence = Ability(2)
    wisdom = Ability(12)
    charisma = Ability(4)
    speed = 5
    swim_speed = 0
    fly_speed = 30
    climb_speed = 0
    burrow_speed = 0
    hp_max = 1
    hit_dice = '1d4 + -1'
    condition_immunities = ''
    damage_immunities = ''
    damage_resistances = ''
    damage_vulnerabilities = ''
    spells = []


class BeardedDevil(Monster):
    """

    Devil's Sight.
      Magical darkness doesn't impede the devil's darkvision.
    Magic Resistance.
      The devil has advantage on saving throws against spells and other
      magical effects.
    Steadfast.
      The devil can't be frightened while it can see an allied creature
      within 30 feet of it.

    # Actions

    Multiattack.
      The devil makes two attacks: one with its beard and one with its
      glaive.
    Beard.
      Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 6 (1d8
      + 2) piercing damage, and the target must succeed on a DC 12
      Constitution saving throw or be poisoned for 1 minute. While poisoned
      in this way, the target can't regain hit points. The target can repeat
      the saving throw at the end of each of its turns, ending the effect on
      itself on a success.
    Glaive.
      Melee Weapon Attack: +5 to hit, reach 10 ft., one target. Hit: 8 (1d10
      + 3) slashing damage. If the target is a creature other than an undead
      or a construct, it must succeed on a DC 12 Constitution saving throw
      or lose 5 (1d10) hit points at the start of each of its turns due to
      an infernal wound. Each time the devil hits the wounded target with
      this attack, the damage dealt by the wound increases by 5 (1d10). Any
      creature can take an action to stanch the wound with a successful DC
      12 Wisdom (Medicine) check. The wound also closes if the target
      receives magical healing.
    """
    name = 'Bearded Devil'
    description = 'Medium fiend, lawful evil'
    challenge_rating = 3
    armor_class = 13
    skills = ''
    senses = 'Darkvision 120 ft., Passive Perception 10'
    languages = 'Infernal, telepathy 120 ft.'
    strength = Ability(16)
    dexterity = Ability(15)
    constitution = Ability(15)
    intelligence = Ability(9)
    wisdom = Ability(11)
    charisma = Ability(11)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    burrow_speed = 0
    hp_max = 52
    hit_dice = '8d8 + 16'
    condition_immunities = 'poisoned'
    damage_immunities = 'fire, poison'
    damage_resistances = 'cold'
    damage_vulnerabilities = ''
    spells = []


class Behir(Monster):
    """

    # Actions

    Multiattack.
      The behir makes two attacks: one with its bite and one to constrict.
    Bite.
      Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 22
      (3d10 + 6) piercing damage.
    Constrict.
      Melee Weapon Attack: +10 to hit, reach 5 ft., one Large or smaller
      creature. Hit: 17 (2d10 + 6) bludgeoning damage plus 17 (2d10 + 6)
      slashing damage. The target is grappled (escape DC 16) if the behir
      isn't already constricting a creature, and the target is restrained
      until this grapple ends.
    Lightning Breath.
      The behir exhales a line of lightning that is 20 ft. long and 5 ft.
      wide. Each creature in that line must make a DC 16 Dexterity saving
      throw, taking 66 (12d10) lightning damage on a failed save, or half as
      much damage on a successful one.
    Swallow.
      The behir makes one bite attack against a Medium or smaller target it
      is grappling. If the attack hits, the target is also swallowed, and
      the grapple ends. While swallowed, the target is blinded and
      restrained, it has total cover against attacks and other effects
      outside the behir, and it takes 21 (6d6) acid damage at the start of
      each of the behir's turns. A behir can have only one creature
      swallowed at a time.
      
      If the behir takes 30 damage or more on a single turn from the
      swallowed creature, the behir must succeed on a DC 14 Constitution
      saving throw at the end of that turn or regurgitate the creature,
      which falls prone in a space within 10 ft. of the behir. If the behir
      dies, a swallowed creature is no longer restrained by it and can
      escape from the corpse by using 15 ft. of movement, exiting prone.
    """
    name = 'Behir'
    description = 'Huge monstrosity, neutral evil'
    challenge_rating = 11
    armor_class = 17
    skills = 'Perception +6, Stealth +7'
    senses = 'Darkvision 90 ft., Passive Perception 16'
    languages = 'Draconic'
    strength = Ability(23)
    dexterity = Ability(16)
    constitution = Ability(18)
    intelligence = Ability(7)
    wisdom = Ability(14)
    charisma = Ability(12)
    speed = 50
    swim_speed = 0
    fly_speed = 0
    climb_speed = 40
    burrow_speed = 0
    hp_max = 168
    hit_dice = '16d12 + 64'
    condition_immunities = ''
    damage_immunities = 'lightning'
    damage_resistances = ''
    damage_vulnerabilities = ''
    spells = []


class Berserker(Monster):
    """

    Reckless.
      At the start of its turn, the berserker can gain advantage on all
      melee weapon attack rolls during that turn, but attack rolls against
      it have advantage until the start of its next turn.

    # Actions

    Greataxe.
      Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 9 (1d12
      + 3) slashing damage.
    """
    name = 'Berserker'
    description = 'Medium humanoid, any chaotic alignment'
    challenge_rating = 2
    armor_class = 13
    skills = ''
    senses = 'Passive Perception 10'
    languages = 'any one language (usually Common)'
    strength = Ability(16)
    dexterity = Ability(12)
    constitution = Ability(17)
    intelligence = Ability(9)
    wisdom = Ability(11)
    charisma = Ability(9)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    burrow_speed = 0
    hp_max = 67
    hit_dice = '9d8 + 27'
    condition_immunities = ''
    damage_immunities = ''
    damage_resistances = ''
    damage_vulnerabilities = ''
    spells = []


class BlackBear(Monster):
    """

    Keen Smell.
      The bear has advantage on Wisdom (Perception) checks that rely on
      smell.

    # Actions

    Multiattack.
      The bear makes two attacks: one with its bite and one with its claws.
    Bite.
      Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 5 (1d6 +
      2) piercing damage.
    Claws.
      Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 7 (2d4 +
      2) slashing damage.
    """
    name = 'Black Bear'
    description = 'Medium beast, unaligned'
    challenge_rating = 0.5
    armor_class = 11
    skills = ''
    senses = 'Passive Perception 13'
    languages = ''
    strength = Ability(15)
    dexterity = Ability(10)
    constitution = Ability(14)
    intelligence = Ability(2)
    wisdom = Ability(12)
    charisma = Ability(7)
    speed = 40
    swim_speed = 0
    fly_speed = 0
    climb_speed = 30
    burrow_speed = 0
    hp_max = 19
    hit_dice = '3d8 + 6'
    condition_immunities = ''
    damage_immunities = ''
    damage_resistances = ''
    damage_vulnerabilities = ''
    spells = []


class BlackDragonWyrmling(Monster):
    """

    Amphibious.
      The dragon can breathe air and water.

    # Actions

    Bite.
      Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (1d10
      + 2) piercing damage plus 2 (1d4) acid damage.
    Acid Breath.
      The dragon exhales acid in a 15-foot line that is 5 feet wide. Each
      creature in that line must make a DC 11 Dexterity saving throw, taking
      22 (Sd8) acid damage on a failed save, or half as much damage on a
      successful one.
    """
    name = 'Black Dragon Wyrmling'
    description = 'Medium dragon, chaotic evil'
    challenge_rating = 2
    armor_class = 17
    skills = 'Perception +4, Stealth +4'
    senses = 'Blindsight 10 ft., Darkvision 60 ft., Passive Perception 14'
    languages = 'Draconic'
    strength = Ability(15)
    dexterity = Ability(14)
    constitution = Ability(13)
    intelligence = Ability(10)
    wisdom = Ability(11)
    charisma = Ability(13)
    speed = 30
    swim_speed = 30
    fly_speed = 60
    climb_speed = 0
    burrow_speed = 0
    hp_max = 33
    hit_dice = '6d8 + 6'
    condition_immunities = ''
    damage_immunities = 'acid'
    damage_resistances = ''
    damage_vulnerabilities = ''
    spells = []


class BlackPudding(Monster):
    """

    Amorphous.
      The pudding can move through a space as narrow as 1 inch wide without
      squeezing.
    Corrosive Form.
      A creature that touches the pudding or hits it with a melee attack
      while within 5 feet of it takes 4 (1d8) acid damage. Any nonmagical
      weapon made of metal or wood that hits the pudding corrodes. After
      dealing damage, the weapon takes a permanent and cumulative -1 penalty
      to damage rolls. If its penalty drops to -5, the weapon is destroyed.
      Nonmagical ammunition made of metal or wood that hits the pudding is
      destroyed after dealing damage. The pudding can eat through 2-inch-
      thick, nonmagical wood or metal in 1 round.
    Spider Climb.
      The pudding can climb difficult surfaces, including upside down on
      ceilings, without needing to make an ability check.

    # Actions

    Pseudopod.
      Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 +
      3) bludgeoning damage plus 18 (4d8) acid damage. In addition,
      nonmagical armor worn by the target is partly dissolved and takes a
      permanent and cumulative -1 penalty to the AC it offers. The armor is
      destroyed if the penalty reduces its AC to 10.

    # Reactions

    Split.
      When a pudding that is Medium or larger is subjected to lightning or
      slashing damage, it splits into two new puddings if it has at least 10
      hit points. Each new pudding has hit points equal to half the original
      pudding's, rounded down. New puddings are one size smaller than the
      original pudding.
    """
    name = 'Black Pudding'
    description = 'Large ooze, unaligned'
    challenge_rating = 4
    armor_class = 7
    skills = ''
    senses = 'Blindsight 60 ft. (blind beyond this radius), Passive Perception 8'
    languages = ''
    strength = Ability(16)
    dexterity = Ability(5)
    constitution = Ability(16)
    intelligence = Ability(1)
    wisdom = Ability(6)
    charisma = Ability(1)
    speed = 20
    swim_speed = 0
    fly_speed = 0
    climb_speed = 20
    burrow_speed = 0
    hp_max = 85
    hit_dice = '10d10 + 30'
    condition_immunities = 'blinded, charmed, blinded, exhaustion, frightened, prone'
    damage_immunities = 'acid, cold, lightning, slashing'
    damage_resistances = ''
    damage_vulnerabilities = ''
    spells = []


class BlinkDog(Monster):
    """

    Keen Hearing and Smell.
      The dog has advantage on Wisdom (Perception) checks that rely on
      hearing or smell.

    # Actions

    Bite.
      Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 +
      1) piercing damage.
    Teleport.
      The dog magically teleports, along with any equipment it is wearing or
      carrying, up to 40 ft. to an unoccupied space it can see. Before or
      after teleporting, the dog can make one bite attack.
    """
    name = 'Blink Dog'
    description = 'Medium fey, lawful good'
    challenge_rating = 0.25
    armor_class = 13
    skills = 'Perception +3, Stealth +5'
    senses = 'Passive Perception 10'
    languages = "Blink Dog, understands Sylvan but can't speak it"
    strength = Ability(12)
    dexterity = Ability(17)
    constitution = Ability(12)
    intelligence = Ability(10)
    wisdom = Ability(13)
    charisma = Ability(11)
    speed = 40
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    burrow_speed = 0
    hp_max = 22
    hit_dice = '4d8 + 4'
    condition_immunities = ''
    damage_immunities = ''
    damage_resistances = ''
    damage_vulnerabilities = ''
    spells = []


class BloodHawk(Monster):
    """

    Keen Sight.
      The hawk has advantage on Wisdom (Perception) checks that rely on
      sight.
    Pack Tactics.
      The hawk has advantage on an attack roll against a creature if at
      least one of the hawk's allies is within 5 ft. of the creature and the
      ally isn't incapacitated.

    # Actions

    Beak.
      Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 +
      2) piercing damage.
    """
    name = 'Blood Hawk'
    description = 'Small beast, unaligned'
    challenge_rating = 0.125
    armor_class = 12
    skills = 'Perception +4'
    senses = 'Passive Perception 14'
    languages = ''
    strength = Ability(6)
    dexterity = Ability(14)
    constitution = Ability(10)
    intelligence = Ability(3)
    wisdom = Ability(14)
    charisma = Ability(5)
    speed = 10
    swim_speed = 0
    fly_speed = 60
    climb_speed = 0
    burrow_speed = 0
    hp_max = 7
    hit_dice = '2d6 + 0'
    condition_immunities = ''
    damage_immunities = ''
    damage_resistances = ''
    damage_vulnerabilities = ''
    spells = []


class BlueDragonWyrmling(Monster):
    """

    # Actions

    Bite.
      Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d10
      + 3) piercing damage plus 3 (1d6) lightning damage.
    Lightning Breath.
      The dragon exhales lightning in a 30-foot line that is 5 feet wide.
      Each creature in that line must make a DC 12 Dexterity saving throw,
      taking 22 (4d10) lightning damage on a failed save, or half as much
      damage on a successful one.
    """
    name = 'Blue Dragon Wyrmling'
    description = 'Medium dragon, lawful evil'
    challenge_rating = 3
    armor_class = 17
    skills = 'Perception +4, Stealth +2'
    senses = 'Blindsight 10 ft., Darkvision 60 ft., Passive Perception 14'
    languages = 'Draconic'
    strength = Ability(17)
    dexterity = Ability(10)
    constitution = Ability(15)
    intelligence = Ability(12)
    wisdom = Ability(11)
    charisma = Ability(15)
    speed = 30
    swim_speed = 0
    fly_speed = 60
    climb_speed = 0
    burrow_speed = 15
    hp_max = 52
    hit_dice = '8d8 + 16'
    condition_immunities = ''
    damage_immunities = 'lightning'
    damage_resistances = ''
    damage_vulnerabilities = ''
    spells = []


class Boar(Monster):
    """

    Charge.
      If the boar moves at least 20 ft. straight toward a target and then
      hits it with a tusk attack on the same turn, the target takes an extra
      3 (1d6) slashing damage. If the target is a creature, it must succeed
      on a DC 11 Strength saving throw or be knocked prone.
    Relentless.
      If the boar takes 7 damage or less that would reduce it to 0 hit
      points, it is reduced to 1 hit point instead.

    # Actions

    Tusk.
      Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1)
      slashing damage.
    """
    name = 'Boar'
    description = 'Medium beast, unaligned'
    challenge_rating = 0.25
    armor_class = 11
    skills = ''
    senses = 'Passive Perception 9'
    languages = ''
    strength = Ability(13)
    dexterity = Ability(11)
    constitution = Ability(12)
    intelligence = Ability(2)
    wisdom = Ability(9)
    charisma = Ability(5)
    speed = 40
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    burrow_speed = 0
    hp_max = 11
    hit_dice = '2d8 + 2'
    condition_immunities = ''
    damage_immunities = ''
    damage_resistances = ''
    damage_vulnerabilities = ''
    spells = []


class BoneDevil(Monster):
    """

    Devil's Sight.
      Magical darkness doesn't impede the devil's darkvision.
    Magic Resistance.
      The devil has advantage on saving throws against spells and other
      magical effects.

    # Actions

    Multiattack.
      The devil makes three attacks: two with its claws and one with its
      sting.
    Claw.
      Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 8 (1d8
      + 4) slashing damage.
    Sting.
      Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 13 (2d8
      + 4) piercing damage plus 17 (5d6) poison damage, and the target must
      succeed on a DC 14 Constitution saving throw or become poisoned for 1
      minute. The target can repeat the saving throw at the end of each of
      its turns, ending the effect on itself on a success .
    """
    name = 'Bone Devil'
    description = 'Large fiend, lawful evil'
    challenge_rating = 12
    armor_class = 19
    skills = 'Deception +7, Insight +6'
    senses = 'Darkvision 120 ft., Passive Perception 9'
    languages = 'Infernal, telepathy 120 ft.'
    strength = Ability(18)
    dexterity = Ability(16)
    constitution = Ability(18)
    intelligence = Ability(13)
    wisdom = Ability(14)
    charisma = Ability(16)
    speed = 40
    swim_speed = 0
    fly_speed = 40
    climb_speed = 0
    burrow_speed = 0
    hp_max = 142
    hit_dice = '15d10 + 60'
    condition_immunities = 'poisoned'
    damage_immunities = 'fire, poison'
    damage_resistances = 'cold'
    damage_vulnerabilities = ''
    spells = []


class BrassDragonWyrmling(Monster):
    """

    # Actions

    Bite.
      Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (1d10
      + 2) piercing damage.
    Breath Weapons.
      The dragon uses one of the following breath weapons.
      
      Fire Breath. The dragon exhales fire in an 20-foot line that is 5 feet
      wide. Each creature in that line must make a DC 11 Dexterity saving
      throw, taking 14 (4d6) fire damage on a failed save, or half as much
      damage on a successful one.
      
      Sleep Breath. The dragon exhales sleep gas in a 15-foot cone. Each
      creature in that area must succeed on a DC 11 Constitution saving
      throw or fall unconscious for 1 minute. This effect ends for a
      creature if the creature takes damage or someone uses an action to
      wake it.
    """
    name = 'Brass Dragon Wyrmling'
    description = 'Medium dragon, chaotic good'
    challenge_rating = 1
    armor_class = 16
    skills = 'Perception +4, Stealth +2'
    senses = 'Blindsight 10 ft., Darkvision 60 ft., Passive Perception 14'
    languages = 'Draconic'
    strength = Ability(15)
    dexterity = Ability(10)
    constitution = Ability(13)
    intelligence = Ability(10)
    wisdom = Ability(11)
    charisma = Ability(13)
    speed = 30
    swim_speed = 0
    fly_speed = 60
    climb_speed = 0
    burrow_speed = 15
    hp_max = 16
    hit_dice = '3d8 + 3'
    condition_immunities = ''
    damage_immunities = 'fire'
    damage_resistances = ''
    damage_vulnerabilities = ''
    spells = []


class BronzeDragonWyrmling(Monster):
    """

    Amphibious.
      The dragon can breathe air and water.

    # Actions

    Bite.
      Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d10
      + 3) piercing damage.
    Breath Weapons.
      The dragon uses one of the following breath weapons.
      
      Lightning Breath. The dragon exhales lightning in a 40-foot line that
      is 5 feet wide. Each creature in that line must make a DC 12 Dexterity
      saving throw, taking 16 (3d10) lightning damage on a failed save, or
      half as much damage on a successful one.
      
      Repulsion Breath. The dragon exhales repulsion energy in a 30-foot
      cone. Each creature in that area must succeed on a DC 12 Strength
      saving throw. On a failed save, the creature is pushed 30 feet away
      from the dragon.
    """
    name = 'Bronze Dragon Wyrmling'
    description = 'Medium dragon, lawful good'
    challenge_rating = 2
    armor_class = 17
    skills = 'Perception +4, Stealth +2'
    senses = 'Blindsight 10 ft., Darkvision 60 ft., Passive Perception 14'
    languages = 'Draconic'
    strength = Ability(17)
    dexterity = Ability(10)
    constitution = Ability(15)
    intelligence = Ability(12)
    wisdom = Ability(11)
    charisma = Ability(15)
    speed = 30
    swim_speed = 30
    fly_speed = 60
    climb_speed = 0
    burrow_speed = 0
    hp_max = 32
    hit_dice = '5d8 + 10'
    condition_immunities = ''
    damage_immunities = 'lightning'
    damage_resistances = ''
    damage_vulnerabilities = ''
    spells = []


class BrownBear(Monster):
    """

    Keen Smell.
      The bear has advantage on Wisdom (Perception) checks that rely on
      smell.

    # Actions

    Multiattack.
      The bear makes two attacks: one with its bite and one with its claws.
    Bite.
      Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4)
      piercing damage.
    Claws.
      Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 11 (2d6
      + 4) slashing damage.
    """
    name = 'Brown Bear'
    description = 'Large beast, unaligned'
    challenge_rating = 1
    armor_class = 11
    skills = 'Perception +3'
    senses = 'Passive Perception 13'
    languages = ''
    strength = Ability(19)
    dexterity = Ability(10)
    constitution = Ability(16)
    intelligence = Ability(2)
    wisdom = Ability(13)
    charisma = Ability(7)
    speed = 40
    swim_speed = 0
    fly_speed = 0
    climb_speed = 30
    burrow_speed = 0
    hp_max = 34
    hit_dice = '4d10 + 12'
    condition_immunities = ''
    damage_immunities = ''
    damage_resistances = ''
    damage_vulnerabilities = ''
    spells = []


class Bugbear(Monster):
    """

    Brute.
      A melee weapon deals one extra die of its damage when the bugbear hits
      with it (included in the attack).
    Surprise Attack.
      If the bugbear surprises a creature and hits it with an attack during
      the first round of combat, the target takes an extra 7 (2d6) damage
      from the attack.

    # Actions

    Morningstar.
      Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 11 (2d8
      + 2) piercing damage.
    Javelin.
      Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120
      ft., one target. Hit: 9 (2d6 + 2) piercing damage in melee or 5 (1d6 +
      2) piercing damage at range.
    """
    name = 'Bugbear'
    description = 'Medium humanoid, chaotic evil'
    challenge_rating = 1
    armor_class = 16
    skills = 'Stealth +6, Survival +2'
    senses = 'Darkvision 60 ft., Passive Perception 10'
    languages = 'Common, Goblin'
    strength = Ability(15)
    dexterity = Ability(14)
    constitution = Ability(13)
    intelligence = Ability(8)
    wisdom = Ability(11)
    charisma = Ability(9)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    burrow_speed = 0
    hp_max = 27
    hit_dice = '5d8 + 5'
    condition_immunities = ''
    damage_immunities = ''
    damage_resistances = ''
    damage_vulnerabilities = ''
    spells = []


class Bulette(Monster):
    """

    Standing Leap.
      The bulette's long jump is up to 30 ft. and its high jump is up to 15
      ft., with or without a running start.

    # Actions

    Bite.
      Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 30 (4d12
      + 4) piercing damage.
    Deadly Leap.
      If the bulette jumps at least 15 ft. as part of its movement, it can
      then use this action to land on its ft. in a space that contains one
      or more other creatures. Each of those creatures must succeed on a DC
      16 Strength or Dexterity saving throw (target's choice) or be knocked
      prone and take 14 (3d6 + 4) bludgeoning damage plus 14 (3d6 + 4)
      slashing damage. On a successful save, the creature takes only half
      the damage, isn't knocked prone, and is pushed 5 ft. out of the
      bulette's space into an unoccupied space of the creature's choice. If
      no unoccupied space is within range, the creature instead falls prone
      in the bulette's space.
    """
    name = 'Bulette'
    description = 'Large monstrosity, unaligned'
    challenge_rating = 5
    armor_class = 17
    skills = 'Perception +6'
    senses = 'Darkvision 60 ft., Tremorsense 60 ft., Passive Perception 16'
    languages = ''
    strength = Ability(19)
    dexterity = Ability(11)
    constitution = Ability(21)
    intelligence = Ability(2)
    wisdom = Ability(10)
    charisma = Ability(5)
    speed = 40
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    burrow_speed = 40
    hp_max = 94
    hit_dice = '9d10 + 45'
    condition_immunities = ''
    damage_immunities = ''
    damage_resistances = ''
    damage_vulnerabilities = ''
    spells = []


class Burrowshark(Monster):
    """
      Elite warriors of the earth cult, burrowsharks are fierce champions
      who ride trained bulettes into battle. While their powerful mounts
      rend and tear foes to pieces, burrowsharks leap to the ground and
      cut down their foes without mercy.
      
      Burrowsharks are much like Black Earth guards, since both have
      uncanny footing and special armor. For burrowsharks, an additional
      gift of Ogremoch's might establishes a magical bond between the
      burrowshark and a bulette, allowing the rider to burrow with its
      mount and sense what its mount senses.

    Bond of the Black Earth.
      The burrowshark is magically bound to a bulette trained to serve
      as its mount. While mounted on its bulette, the burrowshark
      shares the bulette's sense and can ride the bulette while it
      burrows. The bonded bulette obeys the burrowshark's commands. If
      its mount dies, the burrowshark can train a new bulette to serve
      as its bonded mount, a process requiring a month.

    # Actions

    Multiattack.
      The burrowshark makes three melee attacks.
    Spear.
      Melee or ranged weapon attack: +6 to hit, reach 5ft. or range
      20/60ft., one target. Hit: 7 (1d6+4) piercing damage, or 8
      (1d8+4) piercing damage if used with two hands to make a melee
      attack.
    Unyielding.
      When the burrowshark is subjected to an effect that would move
      it, knock it prone, or both, it can use its reaction to be
      neither moved nor knocked prone.
    
    """
    name = 'Burrowshark'
    description = 'Medium humanoid (human), neutral evil'
    challenge_rating = 4
    armor_class = 18
    skills = 'Animal handling +2, Athletics +6, Intimidation + 3, Perception +2'
    senses = 'passive Perception 12'
    languages = 'Common'
    strength = Ability(18)
    dexterity = Ability(12)
    constitution = Ability(16)
    intelligence = Ability(10)
    wisdom = Ability(11)
    charisma = Ability(13)
    speed = 30
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 82
    hit_dice = '11d8+33'
