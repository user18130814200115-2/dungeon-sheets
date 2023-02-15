from dungeonsheets.spells.spells import Spell


class SacredFlame(Spell):
	"""Flame-like radiance descends on a creature that you can see within 
	range. The target must succeed on a Dexterity saving throw or take 1d8 
	radiant damage. The target gains no benefit from cover for this saving 
	throw.The spell's damage increases by 1d8 when you reach 5th level 
	(2d8), 11th level (3d8), and 17th level (4d8).
	
	"""

	name = "Sacred Flame"
	level = "Cantrip"
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V", "S")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Evocation"
	classes = ("Cleric")
class Sanctuary(Spell):
	"""You ward a creature within range against attack. Until the spell 
	ends, any creature who targets the warded creature with an attack or a 
	harmful spell must first make a Wisdom saving throw. On a failed save, 
	the creature must choose a new target or lose the attack or spell. This 
	spell doesn't protect the warded creature from area effects, such as 
	the explosion of a fireball.If the warded creature makes an attack, 
	casts a spell that affects an enemy, or deals damage to another 
	creature, this spell ends.
	
	"""

	name = "Sanctuary"
	level = "1"
	casting_time = "Bonus"
	casting_range = "30 feet"
	components = ("V", "S", "M")
	materials = "a small silver mirror"
	duration = "1 minute"
	ritual = False
	magic_school = "Abjuration"
	classes = ("Artificer", "Cleric")
class SappingSting(Spell):
	"""You sap the vitality of one creature you can see in range. The 
	target must succeed on a Constitution saving throw or take 1d4 necrotic 
	damage and fall prone.This spell's damage increases by 1d4 when you 
	reach 5th level (2d4), 11th level (3d4), and 17th level (4d4).
	
	"""

	name = "Sapping Sting"
	level = "Cantrip"
	casting_time = "Action"
	casting_range = "30 feet"
	components = ("V", "S")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Necromancy"
	classes = ()
class Scatter(Spell):
	"""The air quivers around up to five creatures of your choice that you 
	can see within range. An unwilling creature must succeed on a Wisdom 
	saving throw to resist this spell. You teleport each affected target to 
	an unoccupied space that you can see within 120 feet of you. That space 
	must be on the ground or on a floor.
	
	"""

	name = "Scatter"
	level = "6"
	casting_time = "Action"
	casting_range = "30 feet"
	components = ("V")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Sorcerer", "Warlock", "Wizard")
class ScorchingRay(Spell):
	"""You create three rays of fire and hurl them at targets within range. 
	You can hurl them at one target or several.Make a ranged spell attack 
	for each ray. On a hit, the target takes 2d6 fire damage.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	3rd level or higher, you create one additional ray for each slot level 
	above 2nd."""

	name = "Scorching Ray"
	level = "2"
	casting_time = "Action"
	casting_range = "120 feet"
	components = ("V", "S")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Evocation"
	classes = ("Sorcerer", "Wizard")
class Scrying(Spell):
	"""You can see and hear a particular creature you choose that is on the 
	same plane of existence as you. The target must make a Wisdom saving 
	throw, which is modified by how well you know the target and the sort 
	of physical connection you have to it. If a target knows you're casting 
	this spell, it can fail the saving throw voluntarily if it wants to be 
	observed.Knowledge of TargetKnowledgeSave ModifierSecondhand (you have 
	heard of the target)+5Firsthand (you have met the target)+0Familiar 
	(you know the target well)-5Connection to TargetConnectionSave 
	ModifierLikeness or picture-2Possession or garment-4Body part, lock of 
	hair, bit of nail, or the like-10On a successful save, the target isn't 
	affected, and you can't use this spell against it again for 24 hours.On 
	a failed save, the spell creates an invisible sensor within 10 feet of 
	the target. You can see and hear through the sensor as if you were 
	there. The sensor moves with the target, remaining within 10 feet of it 
	for the duration. A creature that can see invisible objects sees the 
	sensor as a luminous orb about the size of your fist.Instead of 
	targeting a creature, you can choose a location you have seen before as 
	the target of this spell. When you do, the sensor appears at that 
	location and doesn't move.
	
	"""

	name = "Scrying"
	level = "5"
	casting_time = "10 Min."
	casting_range = "Self"
	components = ("V", "S", "M")
	materials = "a focus worth at least 1,000 gp, such as a crystal ball, a silver mirror, or a font filled with holy water"
	duration = "Concentration, up to 10 minutes"
	ritual = False
	magic_school = "Divination"
	classes = ("Bard", "Cleric", "Druid", "Warlock", "Wizard")
class SearingSmite(Spell):
	"""The next time you hit a creature with a melee weapon attack during 
	the spell's duration, your weapon flares with white-hot intensity, and 
	the attack deals an extra 1d6 fire damage to the target and causes the 
	target to ignite in flames. At the start of each of its turns until the 
	spell ends, the target must make a Constitution saving throw. On a 
	failed save, it takes 1d6 fire damage. On a successful save, the spell 
	ends. If the target or a creature within 5 feet of it uses an action to 
	put out the flames, or if some other effect douses the flames (such as 
	the target being submerged in water), the spell ends.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	2nd level or higher, the initial extra damage dealt by the attack 
	increases by 1d6 for each slot level above 1st."""

	name = "Searing Smite"
	level = "1"
	casting_time = "Bonus"
	casting_range = "Self"
	components = ("V")
	materials = ""
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Evocation"
	classes = ("Paladin","Ranger")
class SeeInvisibility(Spell):
	"""For the duration, you see invisible creatures and objects as if they 
	were visible, and you can see into the Ethereal Plane. Ethereal 
	creatures and objects appear ghostly and translucent.
	
	"""

	name = "See Invisibility"
	level = "2"
	casting_time = "Action"
	casting_range = "Self"
	components = ("V", "S", "M")
	materials = "a pinch of talc and a small sprinkling of powdered silver"
	duration = "1 hour"
	ritual = False
	magic_school = "Divination"
	classes = ("Artificer", "Bard", "Sorcerer", "Wizard")
class Seeming(Spell):
	"""This spell allows you to change the appearance of any number of 
	creatures that you can see within range. You give each target you 
	choose a new, illusory appearance. An unwilling target can make a 
	Charisma saving throw, and if it succeeds, it is unaffected by this 
	spell.The spell disguises physical appearance as well as clothing, 
	armor, weapons, and equipment. You can make each creature seem 1 foot 
	shorter or taller and appear thin, fat, or in between. You can't change 
	a target's body type, so you must choose a form that has the same basic 
	arrangement of limbs. Otherwise, the extent of the illusion is up to 
	you. The spell lasts for the duration, unless you use your action to 
	dismiss it sooner.The changes wrought by this spell fail to hold up to 
	physical inspection. For example, if you use this spell to add a hat to 
	a creature's outfit, objects pass through the hat, and anyone who 
	touches it would feel nothing or would feel the creature's head and 
	hair. If you use this spell to appear thinner than you are, the hand of 
	someone who reaches out to touch you would bump into you while it was 
	seemingly still in midair.A creature can use its action to inspect a 
	target and make an Intelligence (Investigation) check against your 
	spell save DC. If it succeeds, it becomes aware that the target is 
	disguised.
	
	"""

	name = "Seeming"
	level = "5"
	casting_time = "Action"
	casting_range = "30 feet"
	components = ("V", "S")
	materials = ""
	duration = "8 hours"
	ritual = False
	magic_school = "Illusion"
	classes = ("Bard", "Sorcerer", "Wizard")
class Sending(Spell):
	"""You send a short message of twenty-five words or less to a creature 
	with which you are familiar. The creature hears the message in its 
	mind, recognizes you as the sender if it knows you, and can answer in a 
	like manner immediately. The spell enables creatures with Intelligence 
	scores of at least 1 to understand the meaning of your message.You can 
	send the message across any distance and even to other planes of 
	existence, but if the target is on a different plane than you, there is 
	a 5 percent chance that the message doesn't arrive.
	
	"""

	name = "Sending"
	level = "3"
	casting_time = "Action"
	casting_range = "Unlimited"
	components = ("V", "S", "M")
	materials = "a short piece of fine copper wire"
	duration = "1 round"
	ritual = False
	magic_school = "Evocation"
	classes = ("Bard", "Cleric", "Wizard")
class SenseEmotionUA(Spell):
	"""You attune your senses to pick up the emotions of others for the 
	duration. When you cast the spell, and as your action on each turn 
	until the spell ends, you can focus your senses on one humanoid you can 
	see within 30 feet of you. You instantly learn the target's prevailing 
	emotion, whether it's love, anger, pain, fear, calm, or something else. 
	If the target isn't actually humanoid or it is immune to being charmed, 
	you sense that it is calm.
	
	"""

	name = "Sense Emotion (UA)"
	level = "1"
	casting_time = "Action"
	casting_range = "Self"
	components = ("V", "S")
	materials = ""
	duration = "Concentration, up to 10 minutes"
	ritual = False
	magic_school = "Divination"
	classes = ("Warlock", "Wizard")
class Sequester(Spell):
	"""By means of this spell, a willing creature or an object can be 
	hidden away, safe from detection for the duration. When you cast the 
	spell and touch the target, it becomes invisible and can't be targeted 
	by divination spells or perceived through scrying sensors created by 
	divination spells.If the target is a creature, it falls into a state of 
	suspended animation. Time ceases to flow for it, and it doesn't grow 
	older.You can set a condition for the spell to end early. The condition 
	can be anything you choose, but it must occur or be visible within 1 
	mile of the target. Examples include ""after 1,000 years"" or ""when 
	the tarrasque awakens."" This spell also ends if the target takes any 
	damage.
	
	"""

	name = "Sequester"
	level = "7"
	casting_time = "Action"
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "a powder composed of diamond, emerald, ruby, and sapphire dust worth at least 5,000 gp, which the spell consumes"
	duration = "Until dispelled"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Wizard")
class ShadowBlade(Spell):
	"""You weave together threads of shadow to create a sword of solidified 
	gloom in your hand. This magic sword lasts until the spell ends. It 
	counts as a simple melee weapon with which you are proficient. It deals 
	2d8 psychic damage on a hit and has the finesse, light, and thrown 
	properties (range 20/60). In addition, when you use the sword to attack 
	a target that is in dim light or darkness, you make the attack roll 
	with advantage.If you drop the weapon or throw it, it dissipates at the 
	end of the turn. Thereafter, while the spell persists, you can use a 
	bonus action to cause the sword to reappear in your hand.
	
	**At Higher Levels:** When you cast this spell using a 3rd- or 
	4th-level spell slot, the damage increases to 3d8. When you cast it 
	using a 5th- or 6th-level spell slot, the damage increases to 4d8. When 
	you cast it using a spell slot of 7th level or higher, the damage 
	increases to 5d8."""

	name = "Shadow Blade"
	level = "2"
	casting_time = "Bonus"
	casting_range = "Self"
	components = ("V", "S")
	materials = ""
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Illusion"
	classes = ("Sorcerer", "Warlock", "Wizard")
class ShadowofMoil(Spell):
	"""Flame-like shadows wreathe your body until the spell ends, causing 
	you to become heavily obscured to others. The shadows turn dim light 
	within 10 feet of you into darkness, and bright light in the same area 
	to dim light.Until the spell ends, you have resistance to radiant 
	damage. In addition, whenever a creature within 10 feet of you hits you 
	with an attack, the shadows lash out at that creature, dealing it 2d8 
	necrotic damage.
	
	"""

	name = "Shadow of Moil"
	level = "4"
	casting_time = "Action"
	casting_range = "Self"
	components = ("V", "S", "M")
	materials = "an undead eyeball encased in a gem worth at least 150 gp"
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Necromancy"
	classes = ("Warlock")
class ShapeWater(Spell):
	"""You choose an area of water that you can see within range and that 
	fits within a 5-foot cube. You manipulate it in one of the following 
	ways:You instantaneously move or otherwise change the flow of the water 
	as you direct, up to 5 feet in any direction. This movement doesn't 
	have enough force to cause damage.You cause the water to form into 
	simple shapes and animate at your direction. This change lasts for 1 
	hour.You change the water's color or opacity. The water must be changed 
	in the same way throughout. This change lasts for 1 hour.You freeze the 
	water, provided that there are no creatures in it. The water unfreezes 
	in 1 hour.If you cast this spell multiple times, you can have no more 
	than two of its non-instantaneous effects active at a time, and you can 
	dismiss such an effect as an action.
	
	"""

	name = "Shape Water"
	level = "Cantrip"
	casting_time = "Action"
	casting_range = "30 feet"
	components = ("S")
	materials = ""
	duration = "Instantaneous or 1 hour (see below)"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Druid", "Sorcerer", "Wizard")
class Shapechange(Spell):
	"""You assume the form of a different creature for the duration. The 
	new form can be of any creature with a challenge rating equal to your 
	level or lower. The creature can't be a construct or an undead, and you 
	must have seen the sort of creature at least once. You transform into 
	an average example of that creature, one without any class levels or 
	the Spellcasting trait.Your game statistics are replaced by the 
	statistics of the chosen creature, though you retain your alignment and 
	Intelligence, Wisdom, and Charisma scores. You also retain all of your 
	skill and saving throw proficiencies, in addition to gaining those of 
	the creature. If the creature has the same proficiency as you and the 
	bonus listed in its statistics is higher than yours, use the creature's 
	bonus in place of yours. You can't use any legendary actions or lair 
	actions of the new form.You assume the hit points and Hit Dice of the 
	new form. When you revert to your normal form, you return to the number 
	of hit points you had before you transformed. If you revert as a result 
	of dropping to 0 hit points, any excess damage carries over to your 
	normal form. As long as the excess damage doesn't reduce your normal 
	form to 0 hit points, you aren't knocked unconscious.You retain the 
	benefit of any features from your class, race, or other source and can 
	use them, provided that your new form is physically capable of doing 
	so. You can't use any special senses you have (for example, darkvision) 
	unless your new form also has that sense. You can only speak if the 
	creature can normally speak.When you transform, you choose whether your 
	equipment falls to the ground, merges into the new form, or is worn by 
	it. Worn equipment functions as normal. The DM determines whether it is 
	practical for the new form to wear a piece of equipment, based on the 
	creature's shape and size. Your equipment doesn't change shape or size 
	to match the new form, and any equipment that the new form can't wear 
	must either fall to the ground or merge into your new form. Equipment 
	that merges has no effect in that state.During this spell's duration, 
	you can use your action to assume a different form following the same 
	restrictions and rules for the original form, with one exception: if 
	your new form has more hit points than your current one, your hit 
	points remain at their current value.
	
	"""

	name = "Shapechange"
	level = "9"
	casting_time = "Action"
	casting_range = "Self"
	components = ("V", "S", "M")
	materials = "a jade circlet worth at least 1,500 gp, which you must place on your head before you cast the spell"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Druid", "Wizard")
class Shatter(Spell):
	"""A sudden loud ringing noise, painfully intense, erupts from a point 
	of your choice within range. Each creature in a 10-foot-radius sphere 
	centered on that point must make a Constitution saving throw. A 
	creature takes 3d8 thunder damage on a failed save, or half as much 
	damage on a successful one. A creature made of inorganic material such 
	as stone, crystal, or metal has disadvantage on this saving throw.A 
	nonmagical object that isn't being worn or carried also takes the 
	damage if it's in the spell's area.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	3rd level or higher, the damage increases by 1d8 for each slot level 
	above 2nd."""

	name = "Shatter"
	level = "2"
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V", "S", "M")
	materials = "a chip of mica"
	duration = "Instantaneous"
	ritual = False
	magic_school = "Evocation"
	classes = ("Bard", "Sorcerer", "Warlock", "Wizard")
class Shield(Spell):
	"""An invisible barrier of magical force appears and protects you. 
	Until the start of your next turn, you have a +5 bonus to AC, including 
	against the triggering attack, and you take no damage from magic 
	missile.
	
	"""

	name = "Shield"
	level = "1"
	casting_time = "Reaction"
	casting_range = "Self"
	components = ("V", "S")
	materials = ""
	duration = "1 round"
	ritual = False
	magic_school = "Abjuration"
	classes = ("Sorcerer", "Wizard")
class ShieldofFaith(Spell):
	"""A shimmering field appears and surrounds a creature of your choice 
	within range, granting it a +2 bonus to AC for the duration.
	
	"""

	name = "Shield of Faith"
	level = "1"
	casting_time = "Bonus"
	casting_range = "60 feet"
	components = ("V", "S", "M")
	materials = "a small parchment with a bit of holy text written on it"
	duration = "Concentration, up to 10 minutes"
	ritual = False
	magic_school = "Abjuration"
	classes = ("Cleric", "Paladin")
class Shillelagh(Spell):
	"""The wood of a club or quarterstaff you are holding is imbued with 
	nature's power. For the duration, you can use your spellcasting ability 
	instead of Strength for the attack and damage rolls of melee attacks 
	using that weapon, and the weapon's damage die becomes a d8. The weapon 
	also becomes magical, if it isn't already. The spell ends if you cast 
	it again or if you let go of the weapon.
	
	"""

	name = "Shillelagh"
	level = "Cantrip"
	casting_time = "Bonus"
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "mistletoe, a shamrock leaf, and a club or quarterstaff"
	duration = "1 minute"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Druid")
class ShockingGrasp(Spell):
	"""Lightning springs from your hand to deliver a shock to a creature 
	you try to touch. Make a melee spell attack against the target. You 
	have advantage on the attack roll if the target is wearing armor made 
	of metal. On a hit, the target takes 1d8 lightning damage, and it can't 
	take reactions until the start of its next turn.The spell's damage 
	increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 
	17th level (4d8).
	
	"""

	name = "Shocking Grasp"
	level = "Cantrip"
	casting_time = "Action"
	casting_range = "Touch"
	components = ("V", "S")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Evocation"
	classes = ("Artificer", "Sorcerer", "Wizard")
class ShutdownUA(Spell):
	"""This spell shuts down all electronic devices within range that are 
	not wielded by or under the direct control of a creature. If an 
	electronic device within range is used by a creature, that creature 
	must succeed on a Constitution saving throw to prevent the device from 
	being shut down. While the spell remains active, no electronic device 
	within range can be started or restarted.
	
	"""

	name = "Shutdown (UA)"
	level = "5"
	casting_time = "Action"
	casting_range = "120 feet"
	components = ("V", "S")
	materials = ""
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Transmutation (technomagic)"
	classes = ("Sorcerer", "Warlock", "Wizard")
class SickeningRadiance(Spell):
	"""Dim, greenish light spreads within a 30-foot-radius sphere centered 
	on a point you choose within range. The light spreads around corners, 
	and it lasts until the spell ends.When a creature moves into the 
	spell's area for the first time on a turn or starts its turn there, 
	that creature must succeed on a Constitution saving throw or take 4d10 
	radiant damage, and it suffers one level of exhaustion and emits a dim, 
	greenish light in a 5-foot radius. This light makes it impossible for 
	the creature to benefit from being invisible. The light and any levels 
	of exhaustion caused by this spell go away when the spell ends.
	
	"""

	name = "Sickening Radiance"
	level = "4"
	casting_time = "Action"
	casting_range = "120 feet"
	components = ("V", "S")
	materials = ""
	duration = "Concentration, up to 10 minutes"
	ritual = False
	magic_school = "Evocation"
	classes = ("Sorcerer", "Warlock", "Wizard")
class Silence(Spell):
	"""For the duration, no sound can be created within or pass through a 
	20-foot-radius sphere centered on a point you choose within range. Any 
	creature or object entirely inside the sphere is immune to thunder 
	damage, and creatures are deafened while entirely inside it. Casting a 
	spell that includes a verbal component is impossible there.
	
	"""

	name = "Silence"
	level = "2"
	casting_time = "Action"
	casting_range = "120 feet"
	components = ("V", "S")
	materials = ""
	duration = "Concentration, up to 10 minutes"
	ritual = True
	magic_school = "Illusion"
	classes = ("Bard", "Cleric", "Ranger")
class SilentImage(Spell):
	"""You create the image of an object, a creature, or some other visible 
	phenomenon that is no larger than a 15-foot cube. The image appears at 
	a spot within range and lasts for the duration. The image is purely 
	visual; it isn't accompanied by sound, smell, or other sensory 
	effects.You can use your action to cause the image to move to any spot 
	within range. As the image changes location, you can alter its 
	appearance so that its movements appear natural for the image. For 
	example, if you create an image of a creature and move it, you can 
	alter the image so that it appears to be walking.Physical interaction 
	with the image reveals it to be an illusion, because things can pass 
	through it. A creature that uses its action to examine the image can 
	determine that it is an illusion with a successful Intelligence 
	(Investigation) check against your spell save DC. If a creature 
	discerns the illusion for what it is, the creature can see through the 
	image.
	
	"""

	name = "Silent Image"
	level = "1"
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V", "S", "M")
	materials = "a bit of fleece"
	duration = "Concentration, up to 10 minutes"
	ritual = False
	magic_school = "Illusion"
	classes = ("Bard", "Sorcerer", "Wizard")
class SilveryBarbs(Spell):
	"""You magically distract the triggering creature and turn its 
	momentary uncertainty into encouragement for another creature. The 
	triggering creature must reroll the d20 and use the lower roll.You can 
	then choose a different creature you can see within range (you can 
	choose yourself). The chosen creature has advantage on the next attack 
	roll, ability check, or saving throw it makes within 1 minute. A 
	creature can be empowered by only one use of this spell at a time.
	
	"""

	name = "Silvery Barbs"
	level = "1"
	casting_time = "Reaction"
	casting_range = "60 feet"
	components = ("V")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Enchantment"
	classes = ("Bard", "Sorcerer", "Wizard")
class Simulacrum(Spell):
	"""You shape an illusory duplicate of one beast or humanoid that is 
	within range for the entire casting time of the spell. The duplicate is 
	a creature, partially real and formed from ice or snow, and it can take 
	actions and otherwise be affected as a normal creature. It appears to 
	be the same as the original, but it has half the creature's hit point 
	maximum and is formed without any equipment. Otherwise, the illusion 
	uses all the statistics of the creature it duplicates, except that it 
	is a construct.The simulacrum is friendly to you and creatures you 
	designate. It obeys your spoken commands, moving and acting in 
	accordance with your wishes and acting on your turn in combat. The 
	simulacrum lacks the ability to learn or become more powerful, so it 
	never increases its level or other abilities, nor can it regain 
	expended spell slots.If the simulacrum is damaged, you can repair it in 
	an alchemical laboratory, using rare herbs and minerals worth 100 gp 
	per hit point it regains. The simulacrum lasts until it drops to 0 hit 
	points, at which point it reverts to snow and melts instantly.If you 
	cast this spell again, any currently active duplicates you created with 
	this spell are instantly destroyed.
	
	"""

	name = "Simulacrum"
	level = "7"
	casting_time = "12 Hr."
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "snow or ice in quantities sufficient to made a life-size copy of the duplicated creature; some hair, fingernail clippings, or other piece of that creature's body placed inside the snow or ice; and powdered ruby worth 1,500 gp, sprinkled over the duplicate and consumed by the spell"
	duration = "Until dispelled"
	ritual = False
	magic_school = "Illusion"
	classes = ("Wizard")
class SkillEmpowerment(Spell):
	"""Your magic deepens a creature's understanding of its own talent. You 
	touch one willing creature and give it expertise in one skill of your 
	choice; until the spell ends, the creature doubles its proficiency 
	bonus for ability checks it makes that use the chosen skill.You must 
	choose a skill in which the target is proficient and that isn't already 
	benefiting from an effect, such as Expertise, that doubles its 
	proficiency bonus.
	
	"""

	name = "Skill Empowerment"
	level = "5"
	casting_time = "Action"
	casting_range = "Touch"
	components = ("V", "S")
	materials = ""
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Artificer", "Bard", "Sorcerer", "Wizard")
class Skywrite(Spell):
	"""You cause up to ten words to form in a part of the sky you can see. 
	The words appear to be made of cloud and remain in place for the 
	spell's duration. The words dissipate when the spell ends. A strong 
	wind can disperse the clouds and end the spell early.
	
	"""

	name = "Skywrite"
	level = "2"
	casting_time = "Action"
	casting_range = "Sight"
	components = ("V", "S")
	materials = ""
	duration = "Concentration, up to 1 hour"
	ritual = True
	magic_school = "Transmutation"
	classes = ("Artificer", "Bard", "Druid", "Wizard")
class Sleep(Spell):
	"""This spell sends creatures into a magical slumber. Roll 5d8; the 
	total is how many hit points of creatures this spell can affect. 
	Creatures within 20 feet of a point you choose within range are 
	affected in ascending order of their current hit points (ignoring 
	unconscious creatures).Starting with the creature that has the lowest 
	current hit points, each creature affected by this spell falls 
	unconscious until the spell ends, the sleeper takes damage, or someone 
	uses an action to shake or slap the sleeper awake. Subtract each 
	creature's hit points from the total before moving on to the creature 
	with the next lowest hit points. A creature's hit points must be equal 
	to or less than the remaining total for that creature to be 
	affected.Undead and creatures immune to being charmed aren't affected 
	by this spell.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	2nd level or higher, roll an additional 2d8 for each slot level above 
	1st."""

	name = "Sleep"
	level = "1"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "a pinch of fine sand, rose petals, or a cricket"
	duration = "1 minute"
	ritual = False
	magic_school = "Enchantment"
	classes = ("Bard", "Sorcerer", "Wizard")
class SleetStorm(Spell):
	"""Until the spell ends, freezing rain and sleet fall in a 20-foot-tall 
	cylinder with a 40-foot radius centered on a point you choose within 
	range. The area is heavily obscured, and exposed flames in the area are 
	doused.The ground in the area is covered with slick ice, making it 
	difficult terrain. When a creature enters the spell's area for the 
	first time on a turn or starts its turn there, it must make a Dexterity 
	saving throw. On a failed save, it falls prone.If a creature starts its 
	turn in the spell's area and is concentrating on a spell, the creature 
	must make a successful Constitution saving throw against your spell 
	save DC or lose concentration.
	
	"""

	name = "Sleet Storm"
	level = "3"
	casting_time = "Action"
	casting_range = "150 feet"
	components = ("V", "S", "M")
	materials = "a pinch of dust and a few drops of water"
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Druid", "Sorcerer", "Wizard")
class Slow(Spell):
	"""You alter time around up to six creatures of your choice in a 
	40-foot cube within range. Each target must succeed on a Wisdom saving 
	throw or be affected by this spell for the duration.An affected 
	target's speed is halved, it takes a −2 penalty to AC and Dexterity 
	saving throws, and it can't use reactions. On its turn, it can use 
	either an action or a bonus action, not both. Regardless of the 
	creature's abilities or magic items, it can't make more than one melee 
	or ranged attack during its turn.If the creature attempts to cast a 
	spell with a casting time of 1 action, roll a d20. On an 11 or higher, 
	the spell doesn't take effect until the creature's next turn, and the 
	creature must use its action on that turn to complete the spell. If it 
	can't, the spell is wasted.A creature affected by this spell makes 
	another Wisdom saving throw at the end of each of its turns. On a 
	successful save, the effect ends for it.
	
	"""

	name = "Slow"
	level = "3"
	casting_time = "Action"
	casting_range = "120 feet"
	components = ("V", "S", "M")
	materials = "a drop of molasses"
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Sorcerer", "Wizard","Bard")
class Snare(Spell):
	"""As you cast this spell, you use the rope to create a circle with a 
	5-foot radius on the ground or the floor. When you finish casting, the 
	rope disappears and the circle becomes a magic trap.This trap is nearly 
	invisible, requiring a successful Intelligence (Investigation) check 
	against your spell save DC to be discerned.The trap triggers when a 
	Small, Medium, or Large creature moves onto the ground or the floor in 
	the spell's radius. That creature must succeed on a Dexterity saving 
	throw or be magically hoisted into the air, leaving it hanging upside 
	down 3 feet above the ground or the floor. The creature is restrained 
	there until the spell ends.A restrained creature can make a Dexterity 
	saving throw at the end of each of its turns, ending the effect on 
	itself on a success. Alternatively, the creature or someone else who 
	can reach it can use an action to make an Intelligence (Arcana) check 
	against your spell save DC. On a success, the restrained effect 
	ends.After the trap is triggered, the spell ends when no creature is 
	restrained by it.
	
	"""

	name = "Snare"
	level = "1"
	casting_time = "1 Min."
	casting_range = "Touch"
	components = ("S", "M")
	materials = "25 feet of rope, which the spell consumes"
	duration = "8 hours"
	ritual = False
	magic_school = "Abjuration"
	classes = ("Artificer", "Druid", "Ranger", "Wizard")
class SnareUA(Spell):
	"""While you cast this spell, you use the cord or rope to create a 
	circle with a 5-foot radius on a flat surface within your reach. When 
	you finish casting, the cord or rope disappears to become a magical 
	trap.The trap is nearly invisible and requires a successful 
	Intelligence (Investigation) check against your spell save DC to be 
	found. The trap triggers when a Small creature or larger moves into the 
	area protected by the spell.The triggering creature must succeed on a 
	Dexterity saving throw or fall prone and be hoisted into the air until 
	it hangs upside down 3 feet above the protected surface, where it is 
	restrained.The restrained creature can make a Dexterity saving throw 
	with disadvantage at the end of each of its turns and ends the 
	restrained effect on a success. Alternatively, another creature that 
	can reach the restrained creature can use an action to make an 
	Intelligence (Arcana) check against your spell save DC. On a success, 
	the restrained effect also ends.
	
	"""

	name = "Snare (UA)"
	level = "1"
	casting_time = "1 Min."
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "30 feet of cord or rope, which is consumed by the spell"
	duration = "Until dispelled or triggered"
	ritual = False
	magic_school = "Abjuration"
	classes = ("Druid", "Ranger", "Wizard")
class SnillocsSnowballSwarm(Spell):
	"""A flurry of magic snowballs erupts from a point you choose within 
	range. Each creature in a 5-foot-radius sphere centered on that point 
	must make a Dexterity saving throw. A creature takes 3d6 cold damage on 
	a failed save, or half as much damage on a successful one.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	3rd level or higher, the damage increases by 1d6 for each slot level 
	above 2nd."""

	name = "Snillocs Snowball Swarm"
	level = "2"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "a piece of ice or a small white rock chip"
	duration = "Instantaneous"
	ritual = False
	magic_school = "Evocation"
	classes = ("Sorcerer", "Wizard")
class SoulCage(Spell):
	"""This spell snatches the soul of a humanoid as it dies and traps it 
	inside the tiny cage you use for the material component. A stolen soul 
	remains inside the cage until the spell ends or until you destroy the 
	cage, which ends the spell. While you have a soul inside the cage, you 
	can exploit it in any of the ways described below. You can use a 
	trapped soul up to six times. Once you exploit a soul for the sixth 
	time, it is released, and the spell ends. While a soul is trapped, the 
	dead humanoid it came from can't be revived. Steal Life. You can use a 
	bonus action to drain vigor from the soul and regain 2d8 hit points. 
	Query Soul. You ask the soul a question (no action required) and 
	receive a brief telepathic answer, which you can understand regardless 
	of the language used. The soul knows only what it knew in life, but it 
	must answer you truthfully and to the best of its ability. The answer 
	is no more than a sentence or two and might be cryptic. Borrow 
	Experience. You can use a bonus action to bolster yourself with the 
	soul's life experience, making your next attack roll, ability check, or 
	saving throw with advantage. If you don't use this benefit before the 
	start of your next turn, it is lost. Eyes of the Dead. You can use an 
	action to name a place the humanoid saw in life, which creates an 
	invisible sensor somewhere in that place if it is on the plane of 
	existence you're currently on. The sensor remains for as long as you 
	concentrate, up to 10 minutes (as if you were concentrating on a 
	spell). You receive visual and auditory information from the sensor as 
	if you were in its space using your senses.A creature that can see the 
	sensor (such as one using see invisibility or truesight) sees a 
	translucent image of the tormented humanoid whose soul you caged.
	
	"""

	name = "Soul Cage"
	level = "6"
	casting_time = "Reaction"
	casting_range = "60 feet"
	components = ("V", "S", "M")
	materials = "a tiny silver cage worth 100 gp"
	duration = "8 hours"
	ritual = False
	magic_school = "Necromancy"
	classes = ("Warlock", "Wizard")
class SparetheDying(Spell):
	"""You touch a living creature that has 0 hit points. The creature 
	becomes stable. This spell has no effect on undead or constructs.
	
	"""

	name = "Spare the Dying"
	level = "Cantrip"
	casting_time = "Action"
	casting_range = "Touch"
	components = ("V", "S")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Necromancy"
	classes = ("Artificer", "Cleric")
class SpeakwithAnimals(Spell):
	"""You gain the ability to comprehend and verbally communicate with 
	beasts for the duration. The knowledge and awareness of many beasts is 
	limited by their intelligence, but at minimum, beasts can give you 
	information about nearby locations and monsters, including whatever 
	they can perceive or have perceived within the past day. You might be 
	able to persuade a beast to perform a small favor for you, at the DM's 
	discretion.
	
	"""

	name = "Speak with Animals"
	level = "1"
	casting_time = "Action"
	casting_range = "Self"
	components = ("V", "S")
	materials = ""
	duration = "10 minutes"
	ritual = True
	magic_school = "Divination"
	classes = ("Bard", "Druid", "Ranger")
class SpeakwithDead(Spell):
	"""You grant the semblance of life and intelligence to a corpse of your 
	choice within range, allowing it to answer the questions you pose. The 
	corpse must still have a mouth and can't be undead. The spell fails if 
	the corpse was the target of this spell within the last 10 days.Until 
	the spell ends, you can ask the corpse up to five questions. The corpse 
	knows only what it knew in life, including the languages it knew. 
	Answers are usually brief, cryptic, or repetitive, and the corpse is 
	under no compulsion to offer a truthful answer if you are hostile to it 
	or it recognizes you as an enemy. This spell doesn't return the 
	creature's soul to its body, only its animating spirit. Thus, the 
	corpse can't learn new information, doesn't comprehend anything that 
	has happened since it died, and can't speculate about future events.
	
	"""

	name = "Speak with Dead"
	level = "3"
	casting_time = "Action"
	casting_range = "10 feet"
	components = ("V", "S", "M")
	materials = "burning incense"
	duration = "10 minutes"
	ritual = False
	magic_school = "Necromancy"
	classes = ("Bard", "Cleric","Wizard")
class SpeakwithPlants(Spell):
	"""You imbue plants within 30 feet of you with limited sentience and 
	animation, giving them the ability to communicate with you and follow 
	your simple commands. You can question plants about events in the 
	spell's area within the past day, gaining information about creatures 
	that have passed, weather, and other circumstances.You can also turn 
	difficult terrain caused by plant growth (such as thickets and 
	undergrowth) into ordinary terrain that lasts for the duration. Or you 
	can turn ordinary terrain where plants are present into difficult 
	terrain that lasts for the duration, causing vines and branches to 
	hinder pursuers, for example.Plants might be able to perform other 
	tasks on your behalf, at the DM's discretion. The spell doesn't enable 
	plants to uproot themselves and move about, but they can freely move 
	branches, tendrils, and stalks.If a plant creature is in the area, you 
	can communicate with it as if you shared a common language, but you 
	gain no magical ability to influence it.This spell can cause the plants 
	created by the entangle spell to release a restrained creature.
	
	"""

	name = "Speak with Plants"
	level = "3"
	casting_time = "Action"
	casting_range = "Self (30-foot radius)"
	components = ("V", "S")
	materials = ""
	duration = "10 minutes"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Bard", "Druid", "Ranger")
class SpiderClimb(Spell):
	"""Until the spell ends, one willing creature you touch gains the 
	ability to move up, down, and across vertical surfaces and upside down 
	along ceilings, while leaving its hands free. The target also gains a 
	climbing speed equal to its walking speed.
	
	"""

	name = "Spider Climb"
	level = "2"
	casting_time = "Action"
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "a drop of bitumen and a spider"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Artificer", "Sorcerer", "Warlock", "Wizard")
class SpikeGrowth(Spell):
	"""The ground in a 20-foot radius centered on a point within range 
	twists and sprouts hard spikes and thorns. The area becomes difficult 
	terrain for the duration. When a creature moves into or within the 
	area, it takes 2d4 piercing damage for every 5 feet it travels.The 
	transformation of the ground is camouflaged to look natural. Any 
	creature that can't see the area at the time the spell is cast must 
	make a Wisdom (Perception) check against your spell save DC to 
	recognize the terrain as hazardous before entering it.
	
	"""

	name = "Spike Growth"
	level = "2"
	casting_time = "Action"
	casting_range = "150 feet"
	components = ("V", "S", "M")
	materials = "seven sharp thorns or seven small twigs, each sharpened to a point"
	duration = "Concentration, up to 10 minutes"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Druid", "Ranger")
class SpiritGuardians(Spell):
	"""You call forth spirits to protect you. They flit around you to a 
	distance of 15 feet for the duration. If you are good or neutral, their 
	spectral form appears angelic or fey (your choice). If you are evil, 
	they appear fiendish.When you cast this spell, you can designate any 
	number of creatures you can see to be unaffected by it. An affected 
	creature's speed is halved in the area, and when the creature enters 
	the area for the first time on a turn or starts its turn there, it must 
	make a Wisdom saving throw. On a failed save, the creature takes 3d8 
	radiant damage (if you are good or neutral) or 3d8 necrotic damage (if 
	you are evil). On a successful save, the creature takes half as much 
	damage.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	4th level or higher, the damage increases by 1d8 for each slot level 
	above 3rd."""

	name = "Spirit Guardians"
	level = "3"
	casting_time = "Action"
	casting_range = "Self (15-foot radius)"
	components = ("V", "S", "M")
	materials = "a holy symbol"
	duration = "Concentration, up to 10 minutes"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Cleric")
class SpiritShroud(Spell):
	"""You call forth spirits of the dead, which flit around you for the 
	spell's duration. The spirits are intangible and invulnerable.Until the 
	spell ends, any attack you make deals 1d8 extra damage when you hit a 
	creature within 10 feet of you. This damage is radiant, necrotic, or 
	cold (your choice when you cast the spell). Any creature that takes 
	this damage can't regain hit points until the start of your next 
	turn.In addition, any creature of your choice that you can see that 
	starts its turn within 10 feet of you has its speed reduced by 10 feet 
	until the start of your next turn.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	4th level or higher, the damage increases by 1d8 for every two slot 
	levels above 3rd."""

	name = "Spirit Shroud"
	level = "3"
	casting_time = "Bonus"
	casting_range = "Self"
	components = ("V", "S")
	materials = ""
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Necromancy"
	classes = (,"Cleric", "Paladin", "Warlock", "Wizard")
class SpiritShroud(Spell):
	"""You call forth spirits of the dead, which flit around you for the 
	spell's duration. The spirits are intangible and invulnerable, and they 
	are good or evil (your choice).Until the spell ends, any attack you 
	make deals 1d8 extra damage when you hit a creature within 10 feet of 
	you. This damage is radiant if the spirits are good and necrotic if 
	they are evil. Any creature that takes this damage can't regain hit 
	points until the start of your next turn.In addition, any creature of 
	your choice that you can see that starts its turn within 10 feet of you 
	has its speed reduced by 10 feet until the start of your next turn.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	4th level or higher, the extra damage increases by 1d8 for each slot 
	level above 3rd."""

	name = "Spirit Shroud"
	level = "3"
	casting_time = "Bonus"
	casting_range = "Self"
	components = ("V", "S")
	materials = ""
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Necromancy"
	classes = ("Cleric", "Paladin", "Warlock", "Wizard")
class SpiritofDeath(Spell):
	"""You call forth a spirit that embodies death itself. Choose a 
	creature you can see within range. The spirit manifests in an 
	unoccupied space that you can see within 10 feet of the target, and the 
	target becomes haunted by the spirit. The spirit uses the Reaper Spirit 
	stat block. The spirit disappears when it or the haunted creature is 
	reduced to 0 hit points, or when the spell ends.The reaper spirit is an 
	ally to you and your companions. In combat, the spirit shares your 
	initiative count, but it takes its turn immediately after yours. It 
	obeys your verbal commands (no action required by you), but it will 
	only attack the haunted creature. If you don't issue the spirit any 
	commands, it takes the Dodge action and uses its move to avoid danger.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	5th level or higher, use the higher level wherever the spell's level 
	appears in the stat block."""

	name = "Spirit of Death"
	level = "4"
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V", "S", "M")
	materials = "a gilded playing card depicting an avatar of death worth at least 400 gp"
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Necromancy"
	classes = ("Sorcerer", "Warlock", "Wizard")
class SpiritualWeapon(Spell):
	"""You create a floating, spectral weapon within range that lasts for 
	the duration or until you cast this spell again. When you cast the 
	spell, you can make a melee spell attack against a creature within 5 
	feet of the weapon. On a hit, the target takes force damage equal to 
	1d8 + your spellcasting ability modifier.As a bonus action on your 
	turn, you can move the weapon up to 20 feet and repeat the attack 
	against a creature within 5 feet of it.The weapon can take whatever 
	form you choose. Clerics of deities who are associated with a 
	particular weapon (as St. Cuthbert is known for his mace and Thor for 
	his hammer) make this spell's effect resemble that weapon.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	3rd level or higher, the damage increases by 1d8 for every two slot 
	levels above 2nd."""

	name = "Spiritual Weapon"
	level = "2"
	casting_time = "Bonus"
	casting_range = "60 feet"
	components = ("V", "S")
	materials = ""
	duration = "1 minute"
	ritual = False
	magic_school = "Evocation"
	classes = ("Cleric")
class SprayofCards(Spell):
	"""You spray spectral cards from your hands or sleeve; the cards blind 
	or slash at your enemies, and then vanish. Choose one of the following 
	effects for the cards. Blinding Cards. Each creature in a 15-foot cone 
	must succeed on a Wisdom saving throw or be blinded until the end of 
	their next turn. Cutting Cards. Each creature in a 15-foot cone must 
	make a Dexterity saving throw. A creature takes 2d10 force damage on a 
	failed save or half as much damage on a successful one.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	4th level or higher, the damage of cutting cards increases by 1d10 for 
	every two slot levels above 2nd."""

	name = "Spray of Cards"
	level = "2"
	casting_time = "Action"
	casting_range = "Self (15-foot cone)"
	components = ("V", "S", "M")
	materials = "a deck of cards"
	duration = "Instantaneous"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Bard", "Sorcerer", "Warlock", "Wizard")
class StaggeringSmite(Spell):
	"""The next time you hit a creature with a melee weapon attack during 
	this spell's duration, your weapon pierces both body and mind, and the 
	attack deals an extra 4d6 psychic damage to the target. The target must 
	make a Wisdom saving throw. On a failed save, it has disadvantage on 
	attack rolls and ability checks, and can't take reactions, until the 
	end of its next turn.
	
	"""

	name = "Staggering Smite"
	level = "4"
	casting_time = "Bonus"
	casting_range = "Self"
	components = ("V")
	materials = ""
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Evocation"
	classes = ("Paladin")
class SteelWindStrike(Spell):
	"""You flourish the weapon used in the casting and then vanish to 
	strike like the wind. Choose up to five creatures you can see within 
	range. Make a melee spell attack against each target. On a hit, a 
	target takes 6d10 force damage.You can then teleport to an unoccupied 
	space you can see within 5 feet of one of the targets you hit or missed.
	
	"""

	name = "Steel Wind Strike"
	level = "5"
	casting_time = "Action"
	casting_range = "30 feet"
	components = ("S", "M")
	materials = "a melee weapon worth at least 1 sp"
	duration = "Instantaneous"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Ranger", "Wizard")
class StinkingCloud(Spell):
	"""You create a 20-foot-radius sphere of yellow, nauseating gas 
	centered on a point within range. The cloud spreads around corners, and 
	its area is heavily obscured. The cloud lingers in the air for the 
	duration.Each creature that is completely within the cloud at the start 
	of its turn must make a Constitution saving throw against poison. On a 
	failed save, the creature spends its action that turn retching and 
	reeling. Creatures that don't need to breathe or are immune to poison 
	automatically succeed on this saving throw.A moderate wind (at least 10 
	miles per hour) disperses the cloud after 4 rounds. A strong wind (at 
	least 20 miles per hour) disperses it after 1 round.
	
	"""

	name = "Stinking Cloud"
	level = "3"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "a rotten egg or several skunk cabbage leaves"
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Bard", "Sorcerer", "Wizard")
class StoneShape(Spell):
	"""You touch a stone object of Medium size or smaller or a section of 
	stone no more than 5 feet in any dimension and form it into any shape 
	that suits your purpose. So, for example, you could shape a large rock 
	into a weapon, idol, or coffer, or make a small passage through a wall, 
	as long as the wall is less than 5 feet thick. You could also shape a 
	stone door or its frame to seal the door shut. The object you create 
	can have up to two hinges and a latch, but finer mechanical detail 
	isn't possible.
	
	"""

	name = "Stone Shape"
	level = "4"
	casting_time = "Action"
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "soft clay, which must be worked into roughly the desired shape of the stone object"
	duration = "Instantaneous"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Artificer", "Cleric", "Druid", "Wizard")
class Stoneskin(Spell):
	"""This spell turns the flesh of a willing creature you touch as hard 
	as stone. Until the spell ends, the target has resistance to nonmagical 
	bludgeoning, piercing, and slashing damage.
	
	"""

	name = "Stoneskin"
	level = "4"
	casting_time = "Action"
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "diamond dust worth 100 gp, which the spell consumes"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Abjuration"
	classes = ("Artificer", "Druid", "Ranger", "Sorcerer", "Wizard")
class StormSphere(Spell):
	"""A 20-foot-radius sphere of whirling air springs into existence, 
	centered on a point you choose within range. The sphere remains for the 
	spell's duration. Each creature in the sphere when it appears or that 
	ends its turn there must succeed on a Strength saving throw or take 2d6 
	bludgeoning damage. The sphere's space is difficult terrain.Until the 
	spell ends, you can use a bonus action on each of your turns to cause a 
	bolt of lightning to leap from the center of the sphere toward one 
	creature you choose within 60 feet of the center. Make a ranged spell 
	attack. You have advantage on the attack roll if the target is in the 
	sphere. On a hit, the target takes 4d6 lightning damage.Creatures 
	within 30 feet of the sphere have disadvantage on Wisdom (Perception) 
	checks made to listen.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	5th level or higher, the damage for each of its effects increases by 
	1d6 for each slot level above 4th."""

	name = "Storm Sphere"
	level = "4"
	casting_time = "Action"
	casting_range = "150 feet"
	components = ("V", "S")
	materials = ""
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Evocation"
	classes = ("Sorcerer", "Wizard")
class StormofVengeance(Spell):
	"""A churning storm cloud forms, centered on a point you can see and 
	spreading to a radius of 360 feet. Lightning flashes in the area, 
	thunder booms, and strong winds roar. Each creature under the cloud (no 
	more than 5,000 feet beneath the cloud) when it appears must make a 
	Constitution saving throw. On a failed save, a creature takes 2d6 
	thunder damage and becomes deafened for 5 minutes.Each round you 
	maintain concentration on this spell, the storm produces different 
	effects on your turn. Round 2. Acidic rain falls from the cloud. Each 
	creature and object under the cloud takes 1d6 acid damage. Round 3. You 
	call six bolts of lightning from the cloud to strike six creatures or 
	objects of your choice beneath the cloud. A given creature or object 
	can't be struck by more than one bolt. A struck creature must make a 
	Dexterity saving throw. The creature takes 10d6 lightning damage on a 
	failed save, or half as much damage on a successful one. Round 4. 
	Hailstones rain down from the cloud. Each creature under the cloud 
	takes 2d6 bludgeoning damage. Round 5–10. Gusts and freezing rain 
	assail the area under the cloud. The area becomes difficult terrain and 
	is heavily obscured. Each creature there takes 1d6 cold damage. Ranged 
	weapon attacks in the area are impossible. The wind and rain count as a 
	severe distraction for the purposes of maintaining concentration on 
	spells. Finally, gusts of strong wind (ranging from 20 to 50 miles per 
	hour) automatically disperse fog, mists, and similar phenomena in the 
	area, whether mundane or magical.
	
	"""

	name = "Storm of Vengeance"
	level = "9"
	casting_time = "Action"
	casting_range = "Sight"
	components = ("V", "S")
	materials = ""
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Druid")
class SuddenAwakeningUA(Spell):
	"""Each sleeping creature you choose within range awakens, and then 
	each prone creature within range can stand up without expending any 
	movement.
	
	"""

	name = "Sudden Awakening (UA)"
	level = "1"
	casting_time = "Bonus"
	casting_range = "10 feet"
	components = ("V")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Enchantment"
	classes = ("Bard", "Ranger", "Sorcerer", "Wizard")
class Suggestion(Spell):
	"""You suggest a course of activity (limited to a sentence or two) and 
	magically influence a creature you can see within range that can hear 
	and understand you. Creatures that can't be charmed are immune to this 
	effect. The suggestion must be worded in such a manner as to make the 
	course of action sound reasonable. Asking the creature to stab itself, 
	throw itself onto a spear, immolate itself, or do some other obviously 
	harmful act ends the spell.The target must make a Wisdom saving throw. 
	On a failed save, it pursues the course of action you described to the 
	best of its ability. The suggested course of action can continue for 
	the entire duration. If the suggested activity can be completed in a 
	shorter time, the spell ends when the subject finishes what it was 
	asked to do.You can also specify conditions that will trigger a special 
	activity during the duration. For example, you might suggest that a 
	knight give her warhorse to the first beggar she meets. If the 
	condition isn't met before the spell expires, the activity isn't 
	performed.If you or any of your companions damage the target, the spell 
	ends.
	
	"""

	name = "Suggestion"
	level = "2"
	casting_time = "Action"
	casting_range = "30 feet"
	components = ("V", "M")
	materials = "a snake's tongue and either a bit of honeycomb or a drop of sweet oil"
	duration = "Concentration, up to 8 hours"
	ritual = False
	magic_school = "Enchantment"
	classes = ("Bard", "Sorcerer", "Warlock", "Wizard")
class SummonAberrantSpirit(Spell):
	"""You call forth a spirit from the Far Realm or another alien realm of 
	madness. The spirit manifests physically in an unoccupied space that 
	you can see within range. This corporeal form uses the Aberrant Spirit 
	stat block. When you cast the spell, choose Beholderkin, Slaadi, or 
	Star Spawn. The creature physically resembles your choice, which also 
	determines some of the traits in its stat block. The creature 
	disappears when it drops to 0 hit points or when the spell ends.The 
	creature is friendly to you and your companions for the spell's 
	duration. In combat, the creature shares your initiative count, but it 
	takes its turn immediately after yours. It obeys verbal commands that 
	you issue to it (no action required by you). If you don't issue any, it 
	defends itself but otherwise takes no action.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	5th level or higher, the creature assumes the higher level for that 
	casting wherever it uses the spell's level in its stat block."""

	name = "Summon Aberrant Spirit"
	level = "4"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "a pickled tentacle and an eyeball in a crystal vial worth at least 400 gp"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Sorcerer", "Warlock", "Wizard")
class SummonAberration(Spell):
	"""You call forth an aberrant spirit. It manifests in an unoccupied 
	space that you can see within range. This corporeal form uses the 
	Aberrant Spirit stat block. When you cast the spell, choose 
	Beholderkin, Slaad, or Star Spawn. The creature resembles an aberration 
	of that kind, which determines certain traits in its stat block. The 
	creature disappears when it drops to 0 hit points or when the spell 
	ends.The creature is an ally to you and your companions. In combat, the 
	creature shares your initiative count, but it takes its turn 
	immediately after yours. It obeys your verbal commands (no action 
	required by you). If you don't issue any, it takes the Dodge action and 
	uses its move to avoid danger.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	5th level or higher, use the higher level wherever the spell's level 
	appears in the stat block."""

	name = "Summon Aberration"
	level = "4"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "a pickled tentacle and an eyeball in a platinum-inlaid vial worth at least 400 gp"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = (,"Warlock", "Wizard")
class SummonBeast(Spell):
	"""You call forth a bestial spirit. It manifests in an unoccupied space 
	that you can see within range. This corporeal form uses the Bestial 
	Spirit stat block. When you cast the spell, choose an environment: Air, 
	Land, or Water. The creature resembles an animal of your choice that is 
	native to the chosen environment, which determines certain traits in 
	its stat block. The creature disappears when it drops to 0 hit points 
	or when the spell ends.The creature is an ally to you and your 
	companions. In combat, the creature shares your initiative count, but 
	it takes its turn immediately after yours. It obeys your verbal 
	commands (no action required by you). If you don't issue any, it takes 
	the Dodge action and uses its move to avoid danger.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	3rd level or higher, use the higher level wherever the spell's level 
	appears in the stat block."""

	name = "Summon Beast"
	level = "2"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "a feather, tuft of fur, and fish tail inside a gilded acorn worth at least 200 gp"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = (,"Druid", "Ranger")
class SummonBestialSpirit(Spell):
	"""You call forth the spirit of a beast. The spirit manifests 
	physically in an unoccupied space that you can see within range. This 
	corporeal form uses the Bestial Spirit stat block. When you cast the 
	spell, choose an environment: Air, Land, or Water. The creature 
	physically resembles an animal of your choice that is native to the 
	chosen environment, which also determines one of the movement modes in 
	the creature's stat block. The creature disappears when it drops to 0 
	hit points or when the spell ends.The creature is friendly to you and 
	your companions for the spell's duration. In combat, the creature 
	shares your initiative count, but it takes its turn immediately after 
	yours. It obeys verbal commands that you issue to it (no action 
	required by you). If you don't issue any, it defends itself but 
	otherwise takes no action.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	3rd level or higher, the creature assumes the higher level for that 
	casting wherever it uses the spell's level in its stat block."""

	name = "Summon Bestial Spirit"
	level = "2"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "a feather, tuft of fur, and fish tail inside a gilded acorn worth at least 200 gp"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Druid", "Ranger")
class SummonCelestial(Spell):
	"""You call forth a celestial spirit. It manifests in an angelic form 
	in an unoccupied space that you can see within range. This corporeal 
	form uses the Celestial Spirit stat block. When you cast the spell, 
	choose Avenger or Defender. Your choice determines the creature's 
	attack in its stat block. The creature disappears when it drops to 0 
	hit points or when the spell ends.The creature is an ally to you and 
	your companions. In combat, the creature shares your initiative count, 
	but it takes its turn immediately after yours. It obeys your verbal 
	commands (no action required by you). If you don't issue any, it takes 
	the Dodge action and uses its move to avoid danger.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	6th level or higher, use the higher level wherever the spell's level 
	appears in the stat block."""

	name = "Summon Celestial"
	level = "5"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "a golden reliquary worth at least 500 gp"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = (,"Cleric", "Paladin")
class SummonCelestialSpirit(Spell):
	"""You call forth a spirit from the Upper Planes. The spirit manifests 
	physically in an angelic form in an unoccupied space that you can see 
	within range. This corporeal form uses the Celestial Spirit stat block. 
	When you cast the spell, choose Avenger or Defender. Your choice 
	determines the creature's attack in its stat block. The creature 
	disappears when it drops to 0 hit points or when the spell ends.The 
	creature is friendly to you and your companions for the spell's 
	duration. In combat, the creature shares your initiative count, but it 
	takes its turn immediately after yours. It obeys verbal commands that 
	you issue to it (no action required by you). If you don't issue any, it 
	defends itself but otherwise takes no action.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	6th level or higher, the creature assumes the higher level for that 
	casting wherever it uses the spell's level in its stat block."""

	name = "Summon Celestial Spirit"
	level = "5"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "a golden reliquary worth at least 500 gp"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Cleric", "Paladin")
class SummonConstruct(Spell):
	"""You call forth the spirit of a construct. It manifests in an 
	unoccupied space that you can see within range. This corporeal form 
	uses the Construct Spirit stat block. When you cast the spell, choose a 
	material: Clay, Metal, or Stone. The creature resembles a golem or a 
	modron (your choice) made of the chosen material, which determines 
	certain traits in its stat block. The creature disappears when it drops 
	to 0 hit points or when the spell ends.The creature is an ally to you 
	and your companions. In combat, the creature shares your initiative 
	count, but it takes its turn immediately after yours. It obeys your 
	verbal commands (no action required by you). If you don't issue any, it 
	takes the Dodge action and uses its move to avoid danger.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	4th level or higher, use the higher level wherever the spell's level 
	appears in the stat block."""

	name = "Summon Construct"
	level = "4"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "an ornate stone and metal lockbox worth at least 400 gp"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Artificer","Wizard")
class SummonDraconicSpirit(Spell):
	"""You call forth a draconic spirit. It manifests in an unoccupied 
	space that you can see within range. This corporeal form uses the 
	Draconic Spirit stat block. When you cast this spell, choose a family 
	of dragon: chromatic, gem, or metallic. The creature resembles a dragon 
	of the chosen family, which determines certain traits in its stat 
	block. The creature disappears when it drops to 0 hit points or when 
	the spell ends.The creature is an ally to you and your companions. In 
	combat, the creature shares your initiative count, but it takes its 
	turn immediately after yours. It obeys your verbal commands (no action 
	required by you). If you don't issue any, it takes the Dodge action and 
	uses its move to avoid danger.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	6th level or higher, use the higher level wherever the spell's level 
	appears in the stat block."""

	name = "Summon Draconic Spirit"
	level = "5"
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V", "S", "M")
	materials = "an object with the image of a dragon engraved on it, worth at least 500 gp"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Druid", "Sorcerer", "Wizard")
class SummonDraconicSpirit(Spell):
	"""You call forth a draconic spirit. It manifests in an unoccupied 
	space that you can see within range.This corporeal form uses the 
	Draconic Spirit stat block. When you cast this spell, choose a family 
	of dragon: Chromatic, Gem, or Metallic. The creature resembles a dragon 
	of the chosen family, which determines certain traits in its stat 
	block. The creature disappears when it drops to 0 hit points or when 
	the spell ends.The creature is an ally to you and your companions. In 
	combat, the creature shares your initiative count, but it takes its 
	turn immediately after yours. It obeys your verbal commands (no action 
	required by you). If you don't issue any, it takes the Dodge action and 
	uses its move to avoid danger.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	6th level or higher, use the higher level wherever the spell's level 
	appears in the stat block."""

	name = "Summon Draconic Spirit"
	level = "5"
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V", "S", "M")
	materials = "an art object from a dragon's hoard, worth at least 500 gp"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Druid", "Sorcerer", "Wizard")
class SummonElemental(Spell):
	"""You call forth an elemental spirit. It manifests in an unoccupied 
	space that you can see within range. This corporeal form uses the 
	Elemental Spirit stat block. When you cast the spell, choose an 
	element: Air, Earth, Fire, or Water. The creature resembles a bipedal 
	form wreathed in the chosen element, which determines certain traits in 
	its stat block. The creature disappears when it drops to 0 hit points 
	or when the spell ends.The creature is an ally to you and your 
	companions. In combat, the creature shares your initiative count, but 
	it takes its turn immediately after yours. It obeys your verbal 
	commands (no action required by you). If you don't issue any, it takes 
	the Dodge action and uses its move to avoid danger.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	5th level or higher, use the higher level wherever the spell's level 
	appears in the stat block."""

	name = "Summon Elemental"
	level = "4"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "air, a pebble, ash, and water inside a gold-inlaid vial worth at least 400 gp"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = (,"Druid", "Ranger", "Wizard")
class SummonElementalSpirit(Spell):
	"""You call forth a spirit from the Elemental Planes. The spirit 
	manifests physically in an unoccupied space that you can see within 
	range. This corporeal form uses the Elemental Spirit stat block. When 
	you cast the spell, choose an element: Air, Earth, Fire, or Water. The 
	creature physically resembles a vaguely humanoid form wreathed in the 
	chosen element, which also determines some of the traits in its stat 
	block. The creature disappears when it drops to 0 hit points or when 
	the spell ends.The creature is friendly to you and your companions for 
	the spell's duration. In combat, the creature shares your initiative 
	count, but it takes its turn immediately after yours. It obeys verbal 
	commands that you issue to it (no action required by you). If you don't 
	issue any, it defends itself but otherwise takes no action.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	5th level or higher, the creature assumes the higher level for that 
	casting wherever it uses the spell's level in its stat block."""

	name = "Summon Elemental Spirit"
	level = "4"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "air, a pebble, ash, and water inside a crystal vial worth at least 400 gp"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Druid", "Sorcerer", "Wizard")
class SummonFey(Spell):
	"""You call forth a fey spirit. It manifests in an unoccupied space 
	that you can see within range. This corporeal form uses the Fey Spirit 
	stat block. When you cast the spell, choose a mood: Fuming, Mirthful, 
	or Tricksy. The creature resembles a fey creature of your choice marked 
	by the chosen mood, which determines one of the traits in its stat 
	block. The creature disappears when it drops to 0 hit points or when 
	the spell ends.The creature is an ally to you and your companions. In 
	combat, the creature shares your initiative count, but it takes its 
	turn immediately after yours. It obeys your verbal commands (no action 
	required by you). If you don't issue any, it takes the Dodge action and 
	uses its move to avoid danger.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	4th level or higher, use the higher level wherever the spell's level 
	appears in the stat block."""

	name = "Summon Fey"
	level = "3"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "a gilded flower worth at least 300 gp"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = (,"Druid", "Ranger", "Warlock", "Wizard")
class SummonFeySpirit(Spell):
	"""You call forth a spirit from the Feywild. The spirit manifests 
	physically in an unoccupied space that you can see within range. This 
	corporeal form uses the Fey Spirit stat block. When you cast the spell, 
	choose a mood: Deceitful, Furious, or Joyful. The creature physically 
	resembles a satyr, a dryad, or an elf (your choice) marked by the 
	chosen mood, which also determines one of the traits in its stat block. 
	The creature disappears when it drops to 0 hit points or when the spell 
	ends.The creature is friendly to you and your companions for the 
	spell's duration. In combat, the creature shares your initiative count, 
	but it takes its turn immediately after yours. It obeys verbal commands 
	that you issue to it (no action required by you). If you don't issue 
	any, it defends itself but otherwise takes no action.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	4th level or higher, the creature assumes the higher level for that 
	casting wherever it uses the spell's level in its stat block."""

	name = "Summon Fey Spirit"
	level = "3"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "a gilded flower worth at least 300 gp"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Bard", "Druid", "Sorcerer", "Warlock", "Wizard")
class SummonFiend(Spell):
	"""You call forth a fiendish spirit. It manifests in an unoccupied 
	space that you can see within range. This corporeal form uses the 
	Fiendish Spirit stat block. When you cast the spell, choose Demon, 
	Devil, or Yugoloth. The creature resembles a fiend of the chosen type, 
	which determines certain traits in its stat block. The creature 
	disappears when it drops to 0 hit points or when the spell ends.The 
	creature is an ally to you and your companions. In combat, the creature 
	shares your initiative count, but it takes its turn immediately after 
	yours. It obeys your verbal commands (no action required by you). If 
	you don't issue any, it takes the Dodge action and uses its move to 
	avoid danger.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	7th level or higher, use the higher level wherever the spell's level 
	appears in the stat block."""

	name = "Summon Fiend"
	level = "6"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "humanoid blood inside a ruby vial worth at least 600 gp"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = (,"Warlock", "Wizard")
class SummonFiendishSpirit(Spell):
	"""You call forth a fiendish spirit from the Lower Planes. The spirit 
	manifests physically in an unoccupied space that you can see within 
	range. This corporeal form uses the Fiendish Spirit stat block. When 
	you cast the spell, choose Demon, Devil, or Yugoloth. The creature 
	physically resembles a fiend of the chosen type, which also determines 
	some of the traits in its stat block. The creature disappears when it 
	drops to 0 hit points or when the spell ends.The creature is friendly 
	to you and your companions for the spell's duration. In combat, the 
	creature shares your initiative count, but it takes its turn 
	immediately after yours. It obeys verbal commands that you issue to it 
	(no action required by you). If you don't issue any, it defends itself 
	but otherwise takes no action.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	7th level or higher, the creature assumes the higher level for that 
	casting wherever it uses the spell's level in its stat block."""

	name = "Summon Fiendish Spirit"
	level = "6"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "humanoid blood inside a ruby vial worth at least 600 gp"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Warlock", "Wizard")
class SummonGreaterDemon(Spell):
	"""You utter foul words, summoning one demon from the chaos of the 
	Abyss. You choose the demon's type, which must be one of challenge 
	rating 5 or lower, such as a shadow demon or a barlgura. The demon 
	appears in an unoccupied space you can see within range, and the demon 
	disappears when it drops to 0 hit points or when the spell ends.Roll 
	initiative for the demon, which has its own turns. When you summon it 
	and on each of your turns thereafter, you can issue a verbal command to 
	it (requiring no action on your part), telling it what it must do on 
	its next turn. If you issue no command, it spends its turn attacking 
	any creature within reach that has attacked it.At the end of each of 
	the demon's turns, it makes a Charisma saving throw. The demon has 
	disadvantage on this saving throw if you say its true name. On a failed 
	save, the demon continues to obey you. On a successful save, your 
	control of the demon ends for the rest of the duration, and the demon 
	spends its turns pursuing and attacking the nearest non-demons to the 
	best of its ability. If you stop concentrating on the spell before it 
	reaches its full duration, an uncontrolled demon doesn't disappear for 
	1d6 rounds if it still has hit points.As part of casting the spell, you 
	can form a circle on the ground with the blood used as a material 
	component. The circle is large enough to encompass your space. While 
	the spell lasts, the summoned demon can't cross the circle or harm it, 
	and it can't target anyone within it. Using the material component in 
	this manner consumes it when the spell ends.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	5th level or higher, the challenge rating increases by 1 for each slot 
	level above 4th."""

	name = "Summon Greater Demon"
	level = "4"
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V", "S", "M")
	materials = "a vial of blood from a humanoid killed within the past 24 hours"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Warlock", "Wizard")
class SummonLesserDemons(Spell):
	"""You utter foul words, summoning demons from the chaos of the Abyss. 
	Roll on the following table to determine what appears.d6Demons 
	Summoned1-2Two demons of challenge rating 1 or lower3-4Four demons of 
	challenge rating 1/2 or lower5-6Eight demons of challenge rating 1/4 or 
	lowerThe DM chooses the demons, such as manes or dretches, and you 
	choose the unoccupied spaces you can see within range where they 
	appear. A summoned demon disappears when it drops to 0 hit points or 
	when the spell ends.The demons are hostile to all creatures, including 
	you. Roll initiative for the summoned demons as a group, which has its 
	own turns. The demons pursue and attack the nearest non-demons to the 
	best of their ability.As part of casting the spell, you can form a 
	circle on the ground with the blood used as a material component. The 
	circle is large enough to encompass your space. While the spell lasts, 
	the summoned demons can't cross the circle or harm it, and they can't 
	target anyone within it. Using the material component in this manner 
	consumes it when the spell ends.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	6th or 7th level, you summon twice as many demons. If you cast it using 
	a spell slot of 8th or 9th level, you summon three times as many 
	demons."""

	name = "Summon Lesser Demons"
	level = "3"
	casting_time = "Action"
	casting_range = "60 feet"
	components = ("V", "S", "M")
	materials = "a vial of blood from a humanoid killed within the past 24 hours"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Warlock", "Wizard")
class SummonShadowSpirit(Spell):
	"""You call forth a shadowy spirit from the Shadowfell. The spirit 
	manifests physically in an unoccupied space that you can see within 
	range. This corporeal form uses the Shadow Spirit stat block. When you 
	cast the spell, choose an emotion: Fury, Despair, or Fear. The creature 
	physically resembles a misshapen humanoid marked by the chosen emotion, 
	which also determines some of the traits in its stat block. The 
	creature disappears when it drops to 0 hit points or when the spell 
	ends.The creature is friendly to you and your companions for the 
	spell's duration. In combat, the creature shares your initiative count, 
	but it takes its turn immediately after yours. It obeys verbal commands 
	that you issue to it (no action required by you). If you don't issue 
	any, it defends itself but otherwise takes no action.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	4th level or higher, the creature assumes the higher level for that 
	casting wherever it uses the spell's level in its stat block."""

	name = "Summon Shadow Spirit"
	level = "3"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "tears inside a crystal vial worth at least 300 gp"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Sorcerer", "Warlock", "Wizard")
class SummonShadowspawn(Spell):
	"""You call forth a shadowy spirit. It manifests in an unoccupied space 
	that you can see within range. This corporeal form uses the Shadow 
	Spirit stat block. When you cast the spell, choose an emotion: Fury, 
	Despair, or Fear. The creature resembles a misshapen biped marked by 
	the chosen emotion, which determines certain traits in its stat block. 
	The creature disappears when it drops to 0 hit points or when the spell 
	ends.The creature is an ally to you and your companions. In combat, the 
	creature shares your initiative count, but it takes its turn 
	immediately after yours. It obeys your verbal commands (no action 
	required by you). If you don't issue any, it takes the Dodge action and 
	uses its move to avoid danger.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	4th level or higher, use the higher level wherever the spell's level 
	appears in the stat block."""

	name = "Summon Shadowspawn"
	level = "3"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "tears inside a gem worth at least 300 gp"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = (,"Warlock", "Wizard")
class SummonUndead(Spell):
	"""You call forth an undead spirit. It manifests in an unoccupied space 
	that you can see within range. This corporeal form uses the Undead 
	Spirit stat block. When you cast the spell, choose the creature's form: 
	Ghostly, Putrid, or Skeletal. The spirit resembles an undead creature 
	with the chosen form, which determines certain traits in its stat 
	block. The creature disappears when it drops to 0 hit points or when 
	the spell ends.The creature is an ally to you and your companions. In 
	combat, the creature shares your initiative count, but it takes its 
	turn immediately after yours. It obeys your verbal commands (no action 
	required by you). If you don't issue any, it takes the Dodge action and 
	uses its move to avoid danger.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	4th level or higher, use the higher level wherever the spell's level 
	appears in the stat block."""

	name = "Summon Undead"
	level = "3"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "a gilded skull worth at least 300 gp"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Necromancy"
	classes = (,"Warlock", "Wizard")
class SummonUndeadSpirit(Spell):
	"""You call forth a restless spirit from beyond the grave. The spirit 
	manifests physically in an unoccupied space that you can see within 
	range. This corporeal form uses the Undead Spirit stat block. When you 
	cast the spell, choose the creature's form: Ghostly, Putrid, or 
	Skeletal. The creature physically resembles a humanoid with the chosen 
	form, which also determines some of the traits in its stat block. The 
	creature disappears when it drops to 0 hit points or when the spell 
	ends.The creature is friendly to you and your companions for the 
	spell's duration. In combat, the creature shares your initiative count, 
	but it takes its turn immediately after yours. It obeys verbal commands 
	that you issue to it (no action required by you). If you don't issue 
	any, it defends itself but otherwise takes no action.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	4th level or higher, the creature assumes the higher level for that 
	casting wherever it uses the spell's level in its stat block."""

	name = "Summon Undead Spirit"
	level = "3"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "a gilded humanoid skull worth at least 300 gp"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Necromancy"
	classes = ("Warlock", "Wizard")
class SummonWarriorSpirit(Spell):
	"""You call forth a warrior spirit from the legendary Deck of Many 
	Things. It manifests in an unoccupied space that you can see within 
	range. This corporeal form uses the Warrior Spirit stat block. When you 
	cast the spell, choose a type of warrior: barbarian, fighter, or monk. 
	The warrior resembles a humanoid armed appropriately to the chosen 
	class, which determines certain traits in its stat block. The warrior 
	disappears when it drops to 0 hit points or when the spell ends.The 
	warrior is an ally to you and your companions. In combat, the warrior 
	shares your initiative count, but it takes its turn immediately after 
	yours. It obeys your verbal commands (no action required by you). If 
	you don't issue any, it takes the Dodge action and uses its move to 
	avoid danger.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	4th level or higher, the creature assumes the higher level for that 
	casting wherever it uses the spell's level in its stat block."""

	name = "Summon Warrior Spirit"
	level = "3"
	casting_time = "Action"
	casting_range = "90 feet"
	components = ("V", "S", "M")
	materials = "a gilded playing card depicting a knight worth at least 300 gp"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Sorcerer", "Warlock", "Wizard")
class Sunbeam(Spell):
	"""A beam of brilliant light flashes out from your hand in a 
	5-foot-wide, 60-foot-long line. Each creature in the line must make a 
	Constitution saving throw. On a failed save, a creature takes 6d8 
	radiant damage and is blinded until your next turn. On a successful 
	save, it takes half as much damage and isn't blinded by this spell. 
	Undead and oozes have disadvantage on this saving throw.You can create 
	a new line of radiance as your action on any turn until the spell 
	ends.For the duration, a mote of brilliant radiance shines in your 
	hand. It sheds bright light in a 30-foot radius and dim light for an 
	additional 30 feet. This light is sunlight.
	
	"""

	name = "Sunbeam"
	level = "6"
	casting_time = "Action"
	casting_range = "Self (60-foot line)"
	components = ("V", "S", "M")
	materials = "a magnifying glass"
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Evocation"
	classes = ("Druid", "Sorcerer", "Wizard","Cleric")
class Sunburst(Spell):
	"""Brilliant sunlight flashes in a 60-foot radius centered on a point 
	you choose within range. Each creature in that light must make a 
	Constitution saving throw. On a failed save, a creature takes 12d6 
	radiant damage and is blinded for 1 minute. On a successful save, it 
	takes half as much damage and isn't blinded by this spell. Undead and 
	oozes have disadvantage on this saving throw.A creature blinded by this 
	spell makes another Constitution saving throw at the end of each of its 
	turns. On a successful save, it is no longer blinded.This spell dispels 
	any darkness in its area that was created by a spell.
	
	"""

	name = "Sunburst"
	level = "8"
	casting_time = "Action"
	casting_range = "150 feet"
	components = ("V", "S", "M")
	materials = "fire and a piece of sunstone"
	duration = "Instantaneous"
	ritual = False
	magic_school = "Evocation"
	classes = ("Druid", "Sorcerer", "Wizard","Cleric")
class SwiftQuiver(Spell):
	"""You transmute your quiver so it produces an endless supply of 
	nonmagical ammunition, which seems to leap into your hand when you 
	reach for it.On each of your turns until the spell ends, you can use a 
	bonus action to make two attacks with a weapon that uses ammunition 
	from the quiver. Each time you make such a ranged attack, your quiver 
	magically replaces the piece of ammunition you used with a similar 
	piece of nonmagical ammunition. Any pieces of ammunition created by 
	this spell disintegrate when the spell ends. If the quiver leaves your 
	possession, the spell ends.
	
	"""

	name = "Swift Quiver"
	level = "5"
	casting_time = "Bonus"
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "a quiver containing at least one piece of ammunition"
	duration = "Concentration, up to 1 minute"
	ritual = False
	magic_school = "Transmutation"
	classes = ("Ranger")
class SwordBurst(Spell):
	"""You create a momentary circle of spectral blades that sweep around 
	you. All other creatures within 5 feet of you must succeed on a 
	Dexterity saving throw or take 1d6 force damage.This spell's damage 
	increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 
	17th level (4d6).
	
	"""

	name = "Sword Burst"
	level = "Cantrip"
	casting_time = "Action"
	casting_range = "Self (5-foot radius)"
	components = ("V")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Conjuration"
	classes = ("Artificer", "Sorcerer", "Warlock", "Wizard","Sorcerer", "Warlock", "Wizard")
class Symbol(Spell):
	"""When you cast this spell, you inscribe a harmful glyph either on a 
	surface (such as a section of floor, a wall, or a table) or within an 
	object that can be closed to conceal the glyph (such as a book, a 
	scroll, or a treasure chest). If you choose a surface, the glyph can 
	cover an area of the surface no larger than 10 feet in diameter. If you 
	choose an object, that object must remain in its place; if the object 
	is moved more than 10 feet from where you cast this spell, the glyph is 
	broken, and the spell ends without being triggered.The glyph is nearly 
	invisible, requiring an Intelligence (Investigation) check against your 
	spell save DC to find it.You decide what triggers the glyph when you 
	cast the spell. For glyphs inscribed on a surface, the most typical 
	triggers include touching or stepping on the glyph, removing another 
	object covering it, approaching within a certain distance of it, or 
	manipulating the object that holds it. For glyphs inscribed within an 
	object, the most common triggers are opening the object, approaching 
	within a certain distance of it, or seeing or reading the glyph.You can 
	further refine the trigger so the spell is activated only under certain 
	circumstances or according to a creature's physical characteristics 
	(such as height or weight), or physical kind (for example, the ward 
	could be set to affect hags or shapechangers). You can also specify 
	creatures that don't trigger the glyph, such as those who say a certain 
	password.When you inscribe the glyph, choose one of the options below 
	for its effect. Once triggered, the glyph glows, filling a 
	60-foot-radius sphere with dim light for 10 minutes, after which time 
	the spell ends. Each creature in the sphere when the glyph activates is 
	targeted by its effect, as is a creature that enters the sphere for the 
	first time on a turn or ends its turn there. Death. Each target must 
	make a Constitution saving throw, taking 10d10 necrotic damage on a 
	failed save, or half as much damage on a successful save. Discord. Each 
	target must make a Constitution saving throw. On a failed save, a 
	target bickers and argues with other creatures for 1 minute. During 
	this time, it is incapable of meaningful communication and has 
	disadvantage on attack rolls and ability checks. Fear. Each target must 
	make a Wisdom saving throw and becomes frightened for 1 minute on a 
	failed save. While frightened, the target drops whatever it is holding 
	and must move at least 30 feet away from the glyph on each of its 
	turns, if able. Hopelessness. Each target must make a Charisma saving 
	throw. On a failed save, the target is overwhelmed with despair for 1 
	minute. During this time, it can't attack or target any creature with 
	harmful abilities, spells, or other magical effects. Insanity. Each 
	target must make an Intelligence saving throw. On a failed save, the 
	target is driven insane for 1 minute. An insane creature can't take 
	actions, can't understand what other creatures say, can't read, and 
	speaks only in gibberish. The DM controls its movement, which is 
	erratic. Pain. Each target must make a Constitution saving throw and 
	becomes incapacitated with excruciating pain for 1 minute on a failed 
	save. Sleep. Each target must make a Wisdom saving throw and falls 
	unconscious for 10 minutes on a failed save. A creature awakens if it 
	takes damage or if someone uses an action to shake or slap it awake. 
	Stunning. Each target must make a Wisdom saving throw and becomes 
	stunned for 1 minute on a failed save.
	
	"""

	name = "Symbol"
	level = "7"
	casting_time = "1 Min."
	casting_range = "Touch"
	components = ("V", "S", "M")
	materials = "mercury, phosphorus, and powdered diamond and opal with a total value of at least 1,000 gp, which the spell consumes"
	duration = "Until dispelled or triggered"
	ritual = False
	magic_school = "Abjuration"
	classes = ("Bard", "Cleric", "Wizard","Druid")
class SynapticStatic(Spell):
	"""You choose a point within range and cause psychic energy to explode 
	there. Each creature in a 20-foot-radius sphere centered on that point 
	must make an Intelligence saving throw. A creature with an Intelligence 
	score of 2 or lower can't be affected by this spell. A target takes 8d6 
	psychic damage on a failed save, or half as much damage on a successful 
	one.After a failed save, a target has muddled thoughts for 1 minute. 
	During that time, it rolls a d6 and subtracts the number rolled from 
	all its attack rolls and ability checks, as well as its Constitution 
	saving throws to maintain concentration. The target can make an 
	Intelligence saving throw at the end of each of its turns, ending the 
	effect on itself on a success.
	
	"""

	name = "Synaptic Static"
	level = "5"
	casting_time = "Action"
	casting_range = "120 feet"
	components = ("V", "S")
	materials = ""
	duration = "Instantaneous"
	ritual = False
	magic_school = "Enchantment"
	classes = ("Bard", "Sorcerer", "Warlock", "Wizard")
class SynchronicityUA(Spell):
	"""The creature you touch feels reality subtly shifted to its favor 
	while this spell is in effect. The target isn't inconvenienced by 
	mundane delays of any sort. Traffic lights are always green, there's 
	always a waiting elevator, and a taxi is always around the corner. The 
	target can run at full speed through dense crowds, and attacks of 
	opportunity provoked by the target's movement are made with 
	disadvantage.Synchronicity grants advantage to Dexterity (Stealth) 
	checks, since the target always finds a handy piece of cover available. 
	Additionally, the target has advantage on all ability checks made to 
	drive a vehicle.In the event that two or more creatures under the 
	effect of synchronicity are attempting to avoid being inconvenienced by 
	each other, the creatures engage in a contest of Charisma each time the 
	effects of the spells would oppose each other.
	
	"""

	name = "Synchronicity (UA)"
	level = "4"
	casting_time = "Action"
	casting_range = "Touch"
	components = ("V", "S")
	materials = ""
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Enchantment"
	classes = ("Sorcerer", "Warlock", "Wizard")
class SystemBackdoorUA(Spell):
	"""This spell allows you to bypass system security in order to create a 
	secure login on a foreign system. The login you create allows you 
	administrator-level privileges in any computer system not enhanced 
	through technomagic. The login defeats any technomagic spells of 3rd 
	level or lower.Once the duration of the spell expires, the login and 
	all privileges are wiped from the system. System logs still show the 
	activity of the user, but the user identification cannot be found or 
	traced.
	
	**At Higher Levels:** When you cast this spell using a spell slot of 
	5th level or higher, you are able to bypass technomagic spells if the 
	spell's level is equal to or less than the level of the spell slot you 
	used."""

	name = "System Backdoor (UA)"
	level = "4"
	casting_time = "1 Min."
	casting_range = "Self"
	components = ("V", "S", "M")
	materials = "hacking tools"
	duration = "Concentration, up to 1 hour"
	ritual = False
	magic_school = "Transmutation (technomagic)"
	classes = ("Sorcerer", "Warlock", "Wizard")
