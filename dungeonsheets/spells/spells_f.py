from dungeonsheets.spells.spells import Spell


class Fabricate(Spell):
	"""You convert raw materials into products of the same material. For 
	example, you can fabricate a wooden bridge from a clump of trees, a 
	rope from a patch of hemp, and clothes from flax or wool.Choose raw 
	materials that you can see within range. You can fabricate a Large or 
	smaller object (contained within a 10-foot cube, or eight connected 
	5-foot cubes), given a sufficient quantity of raw material. If you are 
	working with metal, stone, or another mineral substance, however, the 
	fabricated object can be no larger than Medium (contained within a 
	single 5-foot cube). The quality of objects made by the spell is 
	commensurate with the quality of the raw materials.Creatures or magic 
	items can't be created or transmuted by this spell. You also can't use 
	it to create items that ordinarily require a high degree of 
	craftsmanship, such as jewelry, weapons, glass, or armor, unless you 
	have proficiency with the type of artisan's tools used to craft such 
	objects.
	
	"""

	name = "Fabricate"
	level = 4
	casting_time = "10 Min."
	casting_range = "120 feet"
	components = ("V", "S")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Artificer", "Wizard")
class FaerieFire(Spell):
	"""Each object in a 20-foot cube within range is outlined in blue, 
	green, or violet light (your choice). Any creature in the area when the 
	spell is cast is also outlined in light if it fails a Dexterity saving 
	throw. For the duration, objects and affected creatures shed dim light 
	in a 10-foot radius.Any attack roll against an affected creature or 
	object has advantage if the attacker can see it, and the affected 
	creature or object can't benefit from being invisible.
	
	"""

	name = "Faerie Fire"
	level = 1
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V")
	materials = ""
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Evocation"
	classes = ("Artificer", "Bard", "Druid")
class FalseLife(Spell):
	"""Bolstering yourself with a necromantic facsimile of life, you gain 
	1d4 + 4 temporary hit points for the duration.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	2nd level or higher, you gain 5 additional temporary hit points for 
	each slot level above 1st."""

	name = "False Life"
	level = 1
	casting_time = "Action"
	casting_range = "Self"
	components = ("V", "S", "M")
	materials = "a small amount of alcohol or distilled spirits;"
	duration = "1 hour"
	ritual = False
	magic_school = "Necromancy"
	classes = ("Artificer", "Sorcerer", "Wizard")
class FarStep(Spell):
	"""You teleport up to 60 feet to an unoccupied space you can see. On 
	each of your turns before the spell ends, you can use a bonus action to 
	teleport in this way again.
	
	"""

	name = "Far Step"
	level = 5
	casting_time = "Bonus"
	casting_range = "Self"
	components = ("V")
	materials = ""
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Sorcerer", "Warlock", "Wizard")
class FastFriends(Spell):
	"""When you need to make sure something gets done, you can't rely on 
	vague promises, sworn oaths, or binding contracts of employment. When 
	you cast this spell, choose one humanoid within range that can see and 
	hear you, and that can understand you. The creature must succeed on a 
	Wisdom saving throw or become charmed by you for the duration. While 
	the creature is charmed in this way, it undertakes to perform any 
	services or activities you ask of it in a friendly manner, to the best 
	of its ability.You can set the creature new tasks when a previous task 
	is completed, or if you decide to end its current task. If the service 
	or activity might cause harm to the creature, or if it conflicts with 
	the creature's normal activities and desires, the creature can make 
	another Wisdom saving throw to try to end the effect. This save is made 
	with advantage if you or your companions are fighting the creature. If 
	the activity would result in certain death for the creature, the spell 
	ends.When the spell ends, the creature knows it was charmed by you.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	4th level or higher, you can target one additional creature for each 
	slot level above 3rd."""

	name = "Fast Friends"
	level = 3
	casting_time = "Action"
	casting_range = "30 feet"
	components = ("V")
	materials = ""
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Enchantment"
	classes = ("Bard", "Cleric", "Wizard")
class Fear(Spell):
	"""You project a phantasmal image of a creature's worst fears. Each 
	creature in a 30-foot cone must succeed on a Wisdom saving throw or 
	drop whatever it is holding and become frightened for the 
	duration.While frightened by this spell, a creature must take the Dash 
	action and move away from you by the safest available route on each of 
	its turns, unless there is nowhere to move. If the creature ends its 
	turn in a location where it doesn't have line of sight to you, the 
	creature can make a Wisdom saving throw. On a successful save, the 
	spell ends for that creature.
	
	"""

	name = "Fear"
	level = 3
	casting_time = "Action"
	casting_range = "Self (30-foot cone)"
	components = ("V", "S", "M")
	materials = "a white feather or the heart of a hen;"
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Illusion"
	classes = ("Bard", "Sorcerer", "Warlock", "Wizard")
class FeatherFall(Spell):
	"""Choose up to five falling creatures within range. A falling 
	creature's rate of descent slows to 60 feet per round until the spell 
	ends. If the creature lands before the spell ends, it takes no falling 
	damage and can land on its feet, and the spell ends for that creature.
	
	"""

	name = "Feather Fall"
	level = 1
	casting_time = "Reaction"
	casting_range = "60 feet"
	components = ("V", "M")
	materials = "a small feather or a piece of down;"
	duration = "1 minute"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Artificer", "Bard", "Sorcerer", "Wizard")
class Feeblemind(Spell):
	"""You blast the mind of a creature that you can see within range, 
	attempting to shatter its intellect and personality. The target takes 
	4d6 psychic damage and must make an Intelligence saving throw.On a 
	failed save, the creature's Intelligence and Charisma scores become 1. 
	The creature can't cast spells, activate magic items, understand 
	language, or communicate in any intelligible way. The creature can, 
	however, identify its friends, follow them, and even protect them.At 
	the end of every 30 days, the creature can repeat its saving throw 
	against this spell. If it succeeds on its saving throw, the spell 
	ends.The spell can also be ended by greater restoration, heal, or wish.
	
	"""

	name = "Feeblemind"
	level = 8
	casting_time = "Action"
	casting_range = "150 feet"
	components = ("V", "S", "M")
	materials = "a handful of clay, crystal, glass, or mineral spheres;"
	duration = "Instantaneous"
	ritual = False
	magic_school = "Enchantment"
	classes = ("Bard", "Druid", "Warlock", "Wizard")
class FeignDeath(Spell):
	"""You touch a willing creature and put it into a cataleptic state that 
	is indistinguishable from death.For the spell's duration, or until you 
	use an action to touch the target and dismiss the spell, the target 
	appears dead to all outward inspection and to spells used to determine 
	the target's status. The target is blinded and incapacitated, and its 
	speed drops to 0. The target has resistance to all damage except 
	psychic damage. If the target is diseased or poisoned when you cast the 
	spell, or becomes diseased or poisoned while under the spell's effect, 
	the disease and poison have no effect until the spell ends.
	
	"""

	name = "Feign Death"
	level = 3
	casting_time = "Action"
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "a pinch of graveyard dirt;"
	duration = "1 hour"
	ritual = True
	magic_school = "Necromancy"
	classes = ("Bard", "Cleric", "Druid", "Wizard")
class FindFamiliar(Spell):
	"""You gain the service of a familiar, a spirit that takes an animal 
	form you choose: bat, cat, crab, frog (toad), hawk, lizard, octopus, 
	owl, poisonous snake, fish (quipper), rat, raven, sea horse, spider, or 
	weasel. Appearing in an unoccupied space within range, the familiar has 
	the statistics of the chosen form, though it is a celestial, fey, or 
	fiend (your choice) instead of a beast.Additional animal form choices 
	may be available at the DM's discretion.Your familiar acts 
	independently of you, but it always obeys your commands. In combat, it 
	rolls its own initiative and acts on its own turn. A familiar can't 
	attack, but it can take other actions as normal.When the familiar drops 
	to 0 hit points, it disappears, leaving behind no physical form. It 
	reappears after you cast this spell again. As an action, you can 
	temporarily dismiss the familiar to a pocket dimension. Alternatively, 
	you can dismiss it forever. As an action while it is temporarily 
	dismissed, you can cause it to reappear in any unoccupied space within 
	30 feet of you. Whenever the familiar drops to 0 hit points or 
	disappears into the pocket dimension, it leaves behind in its space 
	anything it was wearing or carrying.While your familiar is within 100 
	feet of you, you can communicate with it telepathically. Additionally, 
	as an action, you can see through your familiar's eyes and hear what it 
	hears until the start of your next turn, gaining the benefits of any 
	special senses that the familiar has. During this time, you are deaf 
	and blind with regard to your own senses.You can't have more than one 
	familiar at a time. If you cast this spell while you already have a 
	familiar, you instead cause it to adopt a new form. Choose one of the 
	forms from the above list. Your familiar transforms into the chosen 
	creature.Finally, when you cast a spell with a range of touch, your 
	familiar can deliver the spell as if it had cast the spell. Your 
	familiar must be within 100 feet of you, and it must use its reaction 
	to deliver the spell when you cast it. If the spell requires an attack 
	roll, you use your attack modifier for the roll.
	
	"""

	name = "Find Familiar"
	level = 1
	casting_time = "1 Hr."
	casting_range = "10 feet"
	components = ("V", "S", "M")
	materials = "10 gp worth of charcoal, incense, and herbs that must be consumed by fire in a brass brazier;"
	duration = "Instantaneous"
	ritual = True
	magic_school = "Conjuration"
	classes = ("Wizard")
class FindGreaterSteed(Spell):
	"""You summon a spirit that assumes the form of a loyal, majestic 
	mount. Appearing in an unoccupied space within range, the spirit takes 
	on a form you choose: a griffon, a pegasus, a peryton, a dire wolf, a 
	rhinoceros, or a saber-toothed tiger. The creature has the statistics 
	provided in the Monster Manual for the chosen form, though it is a 
	celestial, a fey, or a fiend (your choice) instead of its normal 
	creature type. Additionally, if it has an Intelligence score of 5 or 
	lower, its Intelligence becomes 6, and it gains the ability to 
	understand one language of your choice that you speak.You control the 
	mount in combat. While the mount is within 1 mile of you, you can 
	communicate with it telepathically. While mounted on it, you can make 
	any spell you cast that targets only you also target the mount.The 
	mount disappears temporarily when it drops to 0 hit points or when you 
	dismiss it as an action. Casting this spell again re-summons the bonded 
	mount, with all its hit points restored and any conditions removed.You 
	can't have more than one mount bonded by this spell or find steed at 
	the same time. As an action, you can release a mount from its bond, 
	causing it to disappear permanently.Whenever the mount disappears, it 
	leaves behind any objects it was wearing or carrying.Dragonnel Steeds 
	FTD p190[–]With the DM's permission, a paladin can summon a spirit in 
	the form of a dragonnel using the find greater steed spell, which 
	appears in Xanathar's Guide to Everything.
	
	"""

	name = "Find Greater Steed"
	level = 4
	casting_time = "10 Min."
	casting_range = "30 feet"
	components = ("V", "S")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Paladin")
class FindSteed(Spell):
	"""You summon a spirit that assumes the form of an unusually 
	intelligent, strong, and loyal steed, creating a long-lasting bond with 
	it. Appearing in an unoccupied space within range, the steed takes on a 
	form that you choose: a warhorse, a pony, a camel, an elk, or a 
	mastiff. (Your DM might allow other animals to be summoned as steeds.) 
	The steed has the statistics of the chosen form, though it is a 
	celestial, fey, or fiend (your choice) instead of its normal type. 
	Additionally, if your steed has an Intelligence of 5 or less, its 
	Intelligence becomes 6, and it gains the ability to understand one 
	language of your choice that you speak.Your steed serves you as a 
	mount, both in combat and out, and you have an instinctive bond with it 
	that allows you to fight as a seamless unit. While mounted on your 
	steed, you can make any spell you cast that targets only you also 
	target your steed.When the steed drops to 0 hit points, it disappears, 
	leaving behind no physical form. You can also dismiss your steed at any 
	time as an action, causing it to disappear. In either case, casting 
	this spell again summons the same steed, restored to its hit point 
	maximum.While your steed is within 1 mile of you, you can communicate 
	with each other telepathically.You can't have more than one steed 
	bonded by this spell at a time. As an action, you can release the steed 
	from its bond at any time, causing it to disappear.
	
	"""

	name = "Find Steed"
	level = 2
	casting_time = "10 Min."
	casting_range = "30 feet"
	components = ("V", "S")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Paladin")
class FindTraps(Spell):
	"""You sense the presence of any trap within range that is within line 
	of sight. A trap, for the purpose of this spell, includes anything that 
	would inflict a sudden or unexpected effect you consider harmful or 
	undesirable, which was specifically intended as such by its creator. 
	Thus, the spell would sense an area affected by the alarm spell, a 
	glyph of warding, or a mechanical pit trap, but it would not reveal a 
	natural weakness in the floor, an unstable ceiling, or a hidden 
	sinkhole.This spell merely reveals that a trap is present. You don't 
	learn the location of each trap, but you do learn the general nature of 
	the danger posed by a trap you sense.
	
	"""

	name = "Find Traps"
	level = 2
	casting_time = "Action"
	casting_range = "120 feet"
	components = ("V", "S")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Divination"
	classes = ("Cleric", "Druid", "Ranger")
class FindVehicle(Spell):
	"""You summon a spirit that assumes the form of a nonmilitary land 
	vehicle of your choice, appearing in an unoccupied space within range. 
	The vehicle has the statistics of a normal vehicle of its sort, though 
	it is celestial, fey, or fiendish (your choice in origin). The physical 
	characteristics of the vehicle reflect its origin to some degree. For 
	example, a fiendish SUV might be jet black in color, with tinted 
	windows and a sinister-looking front grille.You have a supernatural 
	bond with the conjured vehicle that allows you to drive beyond your 
	normal ability. While driving the conjured vehicle, you are considered 
	proficient with vehicles of its type, and you add double your 
	proficiency bonus to ability checks related to driving the vehicle. 
	While driving the vehicle, you can make any spell you cast that targets 
	only you also target the vehicle.If the vehicle drops to 0 hit points, 
	it disappears, leaving behind no physical form. You can also dismiss 
	the vehicle at any time as an action, causing it to disappear.You can't 
	have more than one vehicle bonded by this spell at a time. As an 
	action, you can release the vehicle from its bond at any time, causing 
	it to disappear.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	3rd level or higher, you can conjure a nonmilitary water vehicle large 
	enough to carry six Medium creatures. When you cast this spell using a 
	spell slot of 5th level or higher, you can conjure a nonmilitary air 
	vehicle large enough to carry ten Medium creatures. When you cast this 
	spell using a spell slot of 7th level or higher, you can conjure any 
	type of vehicle, subject to the DM's approval."""

	name = "Find Vehicle"
	level = 2
	casting_time = "10 Min."
	casting_range = "30 feet"
	components = ("V", "S")
	materials = ""
	duration = "8 hours"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Sorcerer", "Warlock", "Wizard")
class FindThePath(Spell):
	"""This spell allows you to find the shortest, most direct physical 
	route to a specific fixed location that you are familiar with on the 
	same plane of existence. If you name a destination on another plane of 
	existence, a destination that moves (such as a mobile fortress), or a 
	destination that isn't specific (such as ""a green dragon's lair""), 
	the spell fails.For the duration, as long as you are on the same plane 
	of existence as the destination, you know how far it is and in what 
	direction it lies. While you are traveling there, whenever you are 
	presented with a choice of paths along the way, you automatically 
	determine which path is the shortest and most direct route (but not 
	necessarily the safest route) to the destination.
	
	"""

	name = "Find the Path"
	level = 6
	casting_time = "1 Min."
	casting_range = "Self"
	components = ("V", "S", "M")
	materials = "a set of divinatory tools—such as bones, ivory sticks, cards, teeth, or carved runes—worth 100 gp and an object from the location you wish to find;"
	duration = "Concentration, up to 1 day"
	ritual = False
	magic_school = "Divination"
	classes = ("Bard", "Cleric", "Druid")
class FingerOfDeath(Spell):
	"""You send negative energy coursing through a creature that you can 
	see within range, causing it searing pain. The target must make a 
	Constitution saving throw. It takes 7d8 + 30 necrotic damage on a 
	failed save, or half as much damage on a successful one.A humanoid 
	killed by this spell rises at the start of your next turn as a zombie 
	that is permanently under your command, following your verbal orders to 
	the best of its ability.
	
	"""

	name = "Finger of Death"
	level = 7
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V", "S")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Necromancy"
	classes = ("Sorcerer", "Warlock", "Wizard")
class FireBolt(Spell):
	"""You hurl a mote of fire at a creature or object within range. Make a 
	ranged spell attack against the target. On a hit, the target takes 1d10 
	fire damage. A flammable object hit by this spell ignites if it isn't 
	being worn or carried.This spell's damage increases by 1d10 when you 
	reach 5th level (2d10), 11th level (3d10), and 17th level (4d10).
	
	"""

	name = "Fire Bolt"
	level = 0
	casting_time = "Action"
	casting_range = "120 feet"
	components = ("V", "S")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Evocation"
	classes = ("Artificer", "Sorcerer", "Wizard")
class FireShield(Spell):
	"""Thin and wispy flames wreathe your body for the duration, shedding 
	bright light in a 10-foot radius and dim light for an additional 10 
	feet. You can end the spell early by using an action to dismiss it.The 
	flames provide you with a warm shield or a chill shield, as you choose. 
	The warm shield grants you resistance to cold damage, and the chill 
	shield grants you resistance to fire damage.In addition, whenever a 
	creature within 5 feet of you hits you with a melee attack, the shield 
	erupts with flame. The attacker takes 2d8 fire damage from a warm 
	shield, or 2d8 cold damage from a cold shield.
	
	"""

	name = "Fire Shield"
	level = 4
	casting_time = "Action"
	casting_range = "Self"
	components = ("V", "S", "M")
	materials = "a bit of phosphorus or a firefly;"
	duration = "10 minutes"
	ritual = False
	magic_school = "Evocation"
	classes = ("Wizard","Druid", "Sorcerer")
class FireStorm(Spell):
	"""A storm made up of sheets of roaring flame appears in a location you 
	choose within range. The area of the storm consists of up to ten 
	10-foot cubes, which you can arrange as you wish. Each cube must have 
	at least one face adjacent to the face of another cube. Each creature 
	in the area must make a Dexterity saving throw. It takes 7d10 fire 
	damage on a failed save, or half as much damage on a successful one.The 
	fire damages objects in the area and ignites flammable objects that 
	aren't being worn or carried. If you choose, plant life in the area is 
	unaffected by this spell.
	
	"""

	name = "Fire Storm"
	level = 7
	casting_time = "Action"
	casting_range = "150 feet"
	components = ("V", "S")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Evocation"
	classes = ("Cleric", "Druid", "Sorcerer")
class Fireball(Spell):
	"""A bright streak flashes from your pointing finger to a point you 
	choose within range and then blossoms with a low roar into an explosion 
	of flame. Each creature in a 20-foot-radius sphere centered on that 
	point must make a Dexterity saving throw. A target takes 8d6 fire 
	damage on a failed save, or half as much damage on a successful one.The 
	fire spreads around corners. It ignites flammable objects in the area 
	that aren't being worn or carried.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	4th level or higher, the damage increases by 1d6 for each slot level 
	above 3rd."""

	name = "Fireball"
	level = 3
	casting_time = "Action"
	casting_range = "150 feet"
	components = ("V", "S", "M")
	materials = "a tiny ball of bat guano and sulfur;"
	duration = "Instantaneous"
	ritual = False
	magic_school = "Evocation"
	classes = ("Sorcerer", "Wizard")
class FizbansPlatinumShield(Spell):
	"""You create a field of silvery light that surrounds a creature of 
	your choice within range (you can choose yourself). The field sheds dim 
	light out to 5 feet. While surrounded by the field, a creature gains 
	the following benefits:Cover. The creature has half cover.Damage 
	Resistance. The creature has resistance to acid, cold, fire, lightning, 
	and poison damage.Evasion. If the creature is subjected to an effect 
	that allows it to make a Dexterity saving throw to take only half 
	damage, the creature instead takes no damage if it succeeds on the 
	saving throw, and only half damage if it fails.As a bonus action on 
	subsequent turns, you can move the field to another creature within 60 
	feet of the field.
	
	"""

	name = "Fizbans Platinum Shield"
	level = 6
	casting_time = "Bonus"
	casting_range = "60 feet"
	components = ("V", "S", "M")
	materials = "a platinum-plated dragon scale, worth at least 500 gp;"
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Abjuration"
	classes = ("Sorcerer", "Wizard")
class FizbansPlatinumShield(Spell):
	"""You create a field of silvery light that surrounds a creature of 
	your choice within range (you can choose yourself). The field sheds dim 
	light out to 5 feet.As a bonus action on subsequent turns, you can move 
	the field to another creature within 60 feet of the field.The creature 
	protected by the field gains the following benefits:The creature has 
	half cover.The creature has resistance to acid, cold, fire, lightning, 
	and poison damage.If the creature is subjected to an effect that allows 
	it to make a Dexterity saving throw to take only half damage, the 
	creature instead takes no damage if it succeeds on the saving throw, 
	and only half damage if it fails.
	
	"""

	name = "Fizbans Platinum Shield"
	level = 6
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V", "S", "M")
	materials = "a platinum-plated dragon scale, worth at least 500 gp;"
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Abjuration"
	classes = ("Sorcerer", "Wizard")
class FlameArrows(Spell):
	"""You touch a quiver containing arrows or bolts. When a target is hit 
	by a ranged weapon attack using a piece of ammunition drawn from the 
	quiver, the target takes an extra 1d6 fire damage. The spell's magic 
	ends on a piece of ammunition when it hits or misses, and the spell 
	ends when twelve pieces of ammunition have been drawn from the quiver.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	4th level or higher, the number of pieces of ammunition you can affect 
	with this spell increases by two for each slot level above 3rd."""

	name = "Flame Arrows"
	level = 3
	casting_time = "Action"
	casting_range = "Touch"
	components = ("V", "S")
	materials = ""
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Artificer", "Druid", "Ranger", "Sorcerer", "Wizard")
class FlameBlade(Spell):
	"""You evoke a fiery blade in your free hand. The blade is similar in 
	size and shape to a scimitar, and it lasts for the duration. If you let 
	go of the blade, it disappears, but you can evoke the blade again as a 
	bonus action.You can use your action to make a melee spell attack with 
	the fiery blade. On a hit, the target takes 3d6 fire damage.The flaming 
	blade sheds bright light in a 10-foot radius and dim light for an 
	additional 10 feet.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	4th level or higher, the damage increases by 1d6 for every two slot 
	levels above 2nd."""

	name = "Flame Blade"
	level = 2
	casting_time = "Bonus"
	casting_range = "Self"
	components = ("V", "S", "M")
	materials = "leaf of sumac;"
	duration = "Concentration, up to 10 minutes"
	ritual = False
	magic_school = "Evocation"
	classes = ("Druid","Sorcerer")
class FlameStride(Spell):
	"""The billowing flames of a dragon cover your feet, granting you 
	explosive speed. For the duration, your speed increases by 20 feet and 
	moving doesn't provoke opportunity attacks.When you move within 5 feet 
	of a creature or object that isn't being worn or carried, it takes 1d6 
	fire damage from your trail of heat. A creature or object can take this 
	damage only once during a turn.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	4th level or higher, increase your speed by 5 feet for each spell slot 
	level above 3rd. Additionally, the spell deals an additional 1d6 fire 
	damage for each slot level above 3rd."""

	name = "Flame Stride"
	level = 3
	casting_time = "Bonus"
	casting_range = "Self"
	components = ("V", "S")
	materials = ""
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Artificer", "Ranger", "Sorcerer", "Wizard")
class FlameStrike(Spell):
	"""A vertical column of divine fire roars down from the heavens in a 
	location you specify. Each creature in a 10-foot-radius, 40-foot-high 
	cylinder centered on a point within range must make a Dexterity saving 
	throw. A creature takes 4d6 fire damage and 4d6 radiant damage on a 
	failed save, or half as much damage on a successful one.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	6th level or higher, the fire damage or the radiant damage (your 
	choice) increases by 1d6 for each slot level above 5th."""

	name = "Flame Strike"
	level = 5
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V", "S", "M")
	materials = "pinch of sulfur;"
	duration = "Instantaneous"
	ritual = False
	magic_school = "Evocation"
	classes = ("Cleric")
class FlamingSphere(Spell):
	"""A 5-foot-diameter sphere of fire appears in an unoccupied space of 
	your choice within range and lasts for the duration. Any creature that 
	ends its turn within 5 feet of the sphere must make a Dexterity saving 
	throw. The creature takes 2d6 fire damage on a failed save, or half as 
	much damage on a successful one.As a bonus action, you can move the 
	sphere up to 30 feet. If you ram the sphere into a creature, that 
	creature must make the saving throw against the sphere's damage, and 
	the sphere stops moving this turn.When you move the sphere, you can 
	direct it over barriers up to 5 feet tall and jump it across pits up to 
	10 feet wide. The sphere ignites flammable objects not being worn or 
	carried, and it sheds bright light in a 20-foot radius and dim light 
	for an additional 20 feet.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	3rd level or higher, the damage increases by 1d6 for each slot level 
	above 2nd."""

	name = "Flaming Sphere"
	level = 2
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V", "S", "M")
	materials = "a bit of tallow, a pinch of brimstone, and a dusting of powdered iron;"
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Druid", "Wizard","Sorcerer")
class FleshToStone(Spell):
	"""You attempt to turn one creature that you can see within range into 
	stone. If the target's body is made of flesh, the creature must make a 
	Constitution saving throw. On a failed save, it is restrained as its 
	flesh begins to harden. On a successful save, the creature isn't 
	affected.A creature restrained by this spell must make another 
	Constitution saving throw at the end of each of its turns. If it 
	successfully saves against this spell three times, the spell ends. If 
	it fails its saves three times, it is turned to stone and subjected to 
	the petrified condition for the duration. The successes and failures 
	don't need to be consecutive; keep track of both until the target 
	collects three of a kind.If the creature is physically broken while 
	petrified, it suffers from similar deformities if it reverts to its 
	original state.If you maintain your concentration on this spell for the 
	entire possible duration, the creature is turned to stone until the 
	effect is removed.
	
	"""

	name = "Flesh to Stone"
	level = 6
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V", "S", "M")
	materials = "a pinch of lime, water, and earth;"
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Warlock", "Wizard","Druid", "Sorcerer")
class FlockOfFamiliars(Spell):
	"""You temporarily summon three familiars—spirits that take animal 
	forms of your choice. Each familiar uses the same rules and options for 
	a familiar conjured by the find familiar spell. All the familiars 
	conjured by this spell must be the same type of creature (celestials, 
	fey, or fiends; your choice). If you already have a familiar conjured 
	by the find familiar spell or similar means, then one fewer familiars 
	are conjured by this spell.Familiars summoned by this spell can 
	telepathically communicate with you and share their visual or auditory 
	senses while they are within 1 mile of you.When you cast a spell with a 
	range of touch, one of the familiars conjured by this spell can deliver 
	the spell, as normal. However, you can cast a touch spell through only 
	one familiar per turn.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	3rd level or higher, you conjure an additional familiar for each slot 
	level above 2nd."""

	name = "Flock of Familiars"
	level = 2
	casting_time = "1 Min."
	casting_range = "Touch"
	components = ("V", "S")
	materials = ""
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Warlock", "Wizard")
class Fly(Spell):
	"""You touch a willing creature. The target gains a flying speed of 60 
	feet for the duration. When the spell ends, the target falls if it is 
	still aloft, unless it can stop the fall.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	4th level or higher, you can target one additional creature for each 
	slot level above 3rd."""

	name = "Fly"
	level = 3
	casting_time = "Action"
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "a wing feather from any bird;"
	duration = "Concentration, up to 10 minutes"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Artificer", "Sorcerer", "Warlock", "Wizard")
class FogCloud(Spell):
	"""You create a 20-foot-radius sphere of fog centered on a point within 
	range. The sphere spreads around corners, and its area is heavily 
	obscured. It lasts for the duration or until a wind of moderate or 
	greater speed (at least 10 miles per hour) disperses it.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	2nd level or higher, the radius of the fog increases by 20 feet for 
	each slot level above 1st."""

	name = "Fog Cloud"
	level = 1
	casting_time = "Action"
	casting_range = "120 feet"
	components = ("V", "S")
	materials = ""
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Druid", "Ranger", "Sorcerer", "Wizard")
class Forbiddance(Spell):
	"""You create a ward against magical travel that protects up to 40,000 
	square feet of floor space to a height of 30 feet above the floor. For 
	the duration, creatures can't teleport into the area or use portals, 
	such as those created by the gate spell, to enter the area. The spell 
	proofs the area against planar travel, and therefore prevents creatures 
	from accessing the area by way of the Astral Plane, Ethereal Plane, 
	Feywild, Shadowfell, or the plane shift spell.In addition, the spell 
	damages types of creatures that you choose when you cast it. Choose one 
	or more of the following: celestials, elementals, fey, fiends, and 
	undead. When a chosen creature enters the spell's area for the first 
	time on a turn or starts its turn there, the creature takes 5d10 
	radiant or necrotic damage (your choice when you cast this spell).When 
	you cast this spell, you can designate a password. A creature that 
	speaks the password as it enters the area takes no damage from the 
	spell.The spell's area can't overlap with the area of another 
	forbiddance spell. If you cast forbiddance every day for 30 days in the 
	same location, the spell lasts until it is dispelled, and the material 
	components are consumed on the last casting.
	
	"""

	name = "Forbiddance"
	level = 6
	casting_time = "10 Min."
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "a sprinkling of holy water, rare incense, and powdered ruby worth at least 1,000 gp;"
	duration = "1 day"
	ritual = True
	magic_school = "Abjuration"
	classes = ("Cleric")
class Forcecage(Spell):
	"""An immobile, invisible, cube-shaped prison composed of magical force 
	springs into existence around an area you choose within range. The 
	prison can be a cage or a solid box as you choose.A prison in the shape 
	of a cage can be up to 20 feet on a side and is made from 1/2-inch 
	diameter bars spaced 1/2 inch apart.A prison in the shape of a box can 
	be up to 10 feet on a side, creating a solid barrier that prevents any 
	matter from passing through it and blocking any spells cast into or out 
	from the area.When you cast the spell, any creature that is completely 
	inside the cage's area is trapped. Creatures only partially within the 
	area, or those too large to fit inside the area, are pushed away from 
	the center of the area until they are completely outside the area.A 
	creature inside the cage can't leave it by nonmagical means. If the 
	creature tries to use teleportation or interplanar travel to leave the 
	cage, it must first make a Charisma saving throw. On a success, the 
	creature can use that magic to exit the cage. On a failure, the 
	creature can't exit the cage and wastes the use of the spell or effect. 
	The cage also extends into the Ethereal Plane, blocking ethereal 
	travel.This spell can't be dispelled by dispel magic.
	
	"""

	name = "Forcecage"
	level = 7
	casting_time = "Action"
	casting_range = "100 feet"
	components = ("V", "S", "M")
	materials = "ruby dust worth 1,500 gp;"
	duration = "1 hour"
	ritual = False
	magic_school = "Evocation"
	classes = ("Bard", "Warlock", "Wizard")
class Foresight(Spell):
	"""You touch a willing creature and bestow a limited ability to see 
	into the immediate future. For the duration, the target can't be 
	surprised and has advantage on attack rolls, ability checks, and saving 
	throws. Additionally, other creatures have disadvantage on attack rolls 
	against the target for the duration.This spell immediately ends if you 
	cast it again before its duration ends.
	
	"""

	name = "Foresight"
	level = 9
	casting_time = "1 Min."
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "a hummingbird feather;"
	duration = "8 hours"
	ritual = False
	magic_school = "Divination"
	classes = ("Bard", "Druid", "Warlock", "Wizard")
class FortunesFavor(Spell):
	"""You impart latent luck to yourself or one willing creature you can 
	see within range. When the chosen creature makes an attack roll, an 
	ability check, or a saving throw before the spell ends, it can dismiss 
	this spell on itself to roll an additional d20 and choose which of the 
	d20s to use. Alternatively, when an attack roll is made against the 
	chosen creature, it can dismiss this spell on itself to roll a d20 and 
	choose which of the d20s to use, the one it rolled or the one the 
	attacker rolled.If the original d20 roll has advantage or disadvantage, 
	the creature rolls the additional d20 after advantage or disadvantage 
	has been applied to the original roll.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	3rd level or higher, you can target one additional creature for each 
	slot level above 2nd."""

	name = "Fortunes Favor"
	level = 2
	casting_time = "1 Min."
	casting_range = "60 feet"
	components = ("V", "S", "M")
	materials = "a white pearl worth at least 100 gp, which the spell consumes;"
	duration = "1 hour"
	ritual = False
	magic_school = "Divination"
	classes = ()
class FreedomOfMovement(Spell):
	"""You touch a willing creature. For the duration, the target's 
	movement is unaffected by difficult terrain, and spells and other 
	magical effects can neither reduce the target's speed nor cause the 
	target to be paralyzed or restrained.The target can also spend 5 feet 
	of movement to automatically escape from nonmagical restraints, such as 
	manacles or a creature that has it grappled. Finally, being underwater 
	imposes no penalties on the target's movement or attacks.
	
	"""

	name = "Freedom of Movement"
	level = 4
	casting_time = "Action"
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "a leather strap, bound around the arm or a similar appendage;"
	duration = "1 hour"
	ritual = False
	magic_school = "Abjuration"
	classes = ("Artificer", "Bard", "Cleric", "Druid", "Ranger")
class Friends(Spell):
	"""For the duration, you have advantage on all Charisma checks directed 
	at one creature of your choice that isn't hostile toward you. When the 
	spell ends, the creature realizes that you used magic to influence its 
	mood and becomes hostile toward you. A creature prone to violence might 
	attack you. Another creature might seek retribution in other ways (at 
	the DM's discretion), depending on the nature of your interaction with 
	it.
	
	"""

	name = "Friends"
	level = 0
	casting_time = "Action"
	casting_range = "Self"
	components = ("S", "M")
	materials = "a small amount of makeup applied to the face as this spell is cast;"
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Enchantment"
	classes = ("Bard", "Sorcerer", "Warlock", "Wizard")
class FrostFingers(Spell):
	"""Freezing cold blasts from your fingertips in a 15-foot cone. Each 
	creature in that area must make a Constitution saving throw, taking 2d8 
	cold damage on a failed save, or half as much damage on a successful 
	one.The cold freezes nonmagical liquids in the area that aren't being 
	worn or carried.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	2nd level or higher, the damage increases by 1d8 for each slot level 
	above 1st."""

	name = "Frost Fingers"
	level = 1
	casting_time = "Action"
	casting_range = "Self (15-foot cone)"
	components = ("V", "S")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Evocation"
	classes = ("Wizard")
class Frostbite(Spell):
	"""You cause numbing frost to form on one creature that you can see 
	within range. The target must make a Constitution saving throw. On a 
	failed save, the target takes 1d6 cold damage, and it has disadvantage 
	on the next weapon attack roll it makes before the end of its next 
	turn.The spell's damage increases by 1d6 when you reach 5th level 
	(2d6), 11th level (3d6), and 17th level (4d6).
	
	"""

	name = "Frostbite"
	level = 0
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V", "S")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Evocation"
	classes = ("Artificer", "Druid", "Sorcerer", "Warlock", "Wizard")
