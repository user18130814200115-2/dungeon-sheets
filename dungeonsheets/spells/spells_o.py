from dungeonsheets.spells.spells import Spell


class OnOff(Spell):
	"""This cantrip allows you to activate or deactivate any electronic 
	device within range, as long as the device has a clearly defined on or 
	off function that can be easily accessed from the outside of the 
	device. Any device that requires a software-based shutdown sequence to 
	activate or deactivate cannot be affected by on/off.
	
	"""

	name = "On/Off"
	level = 0
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V", "S")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Transmutation (technomagic)"
	classes = ("Sorcerer", "Warlock", "Wizard")
class OtherworldlyForm(Spell):
	"""Uttering an incantation, you draw on the magic of the Lower Planes 
	or Upper Planes (your choice) to transform yourself. You gain the 
	following benefits until the spell ends:You are immune to fire and 
	poison damage (Lower Planes) or radiant and necrotic damage (Upper 
	Planes).You are immune to the poisoned condition (Lower Planes) or the 
	charmed condition (Upper Planes).Spectral wings appear on your back, 
	giving you a flying speed of 40 feet.You have a +2 bonus to AC.All your 
	weapon attacks are magical, and when you make a weapon attack, you can 
	use your spellcasting ability modifier, instead of Strength or 
	Dexterity, for the attack and damage rolls.You can attack twice, 
	instead of once, when you take the Attack action on your turn. You 
	ignore this benefit if you already have a feature, like Extra Attack, 
	that gives you extra attacks.
	
	"""

	name = "Otherworldly Form"
	level = 6
	casting_time = "Action"
	casting_range = "Self"
	components = ("V", "S", "M")
	materials = "an object engraved with a symbol of the Outer Planes, worth at least 500 gp;"
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Cleric", "Sorcerer", "Warlock", "Wizard")
class OtilukesFreezingSphere(Spell):
	"""A frigid globe of cold energy streaks from your fingertips to a 
	point of your choice within range, where it explodes in a 
	60-foot-radius sphere. Each creature within the area must make a 
	Constitution saving throw. On a failed save, a creature takes 10d6 cold 
	damage. On a successful save, it takes half as much damage.If the globe 
	strikes a body of water or a liquid that is principally water (not 
	including water-based creatures), it freezes the liquid to a depth of 6 
	inches over an area 30 feet square. This ice lasts for 1 minute. 
	Creatures that were swimming on the surface of frozen water are trapped 
	in the ice. A trapped creature can use an action to make a Strength 
	check against your spell save DC to break free.You can refrain from 
	firing the globe after completing the spell, if you wish. A small globe 
	about the size of a sling stone, cool to the touch, appears in your 
	hand. At any time, you or a creature you give the globe to can throw 
	the globe (to a range of 40 feet) or hurl it with a sling (to the 
	sling's normal range). It shatters on impact, with the same effect as 
	the normal casting of the spell. You can also set the globe down 
	without shattering it. After 1 minute, if the globe hasn't already 
	shattered, it explodes.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	7th level or higher, the damage increases by 1d6 for each slot level 
	above 6th."""

	name = "Otilukes Freezing Sphere"
	level = 6
	casting_time = "Action"
	casting_range = "300 feet"
	components = ("V", "S", "M")
	materials = "a small crystal sphere;"
	duration = "Instantaneous"
	ritual = False
	magic_school = "Evocation"
	classes = ("Wizard","Sorcerer")
class OtilukesResilientSphere(Spell):
	"""A sphere of shimmering force encloses a creature or object of Large 
	size or smaller within range. An unwilling creature must make a 
	Dexterity saving throw. On a failed save, the creature is enclosed for 
	the duration.Nothing—not physical objects, energy, or other spell 
	effects—can pass through the barrier, in or out, though a creature in 
	the sphere can breathe there. The sphere is immune to all damage, and a 
	creature or object inside can't be damaged by attacks or effects 
	originating from outside, nor can a creature inside the sphere damage 
	anything outside it.The sphere is weightless and just large enough to 
	contain the creature or object inside. An enclosed creature can use its 
	action to push against the sphere's walls and thus roll the sphere at 
	up to half the creature's speed. Similarly, the globe can be picked up 
	and moved by other creatures.A disintegrate spell targeting the globe 
	destroys it without harming anything inside it.
	
	"""

	name = "Otilukes Resilient Sphere"
	level = 4
	casting_time = "Action"
	casting_range = "30 feet"
	components = ("V", "S", "M")
	materials = "a hemispherical piece of clear crystal and a matching hemispherical piece of gum arabic;"
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Evocation"
	classes = ("Artificer", "Wizard")
class OttosIrresistibleDance(Spell):
	"""Choose one creature that you can see within range. The target begins 
	a comic dance in place: shuffling, tapping its feet, and capering for 
	the duration. Creatures that can't be charmed are immune to this 
	spell.A dancing creature must use all its movement to dance without 
	leaving its space and has disadvantage on Dexterity saving throws and 
	attack rolls. While the target is affected by this spell, other 
	creatures have advantage on attack rolls against it. As an action, a 
	dancing creature makes a Wisdom saving throw to regain control of 
	itself. On a successful save, the spell ends.
	
	"""

	name = "Ottos Irresistible Dance"
	level = 6
	casting_time = "Action"
	casting_range = "30 feet"
	components = ("V")
	materials = ""
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Enchantment"
	classes = ("Bard", "Wizard")
