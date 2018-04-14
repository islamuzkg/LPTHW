# For more details, please see link below.
# https://ugoproto.github.io/ugo_py_doc/Learn%20Python%20the%20Hard%20Way/#exercise-45-you-make-a-game
from sys import exit
from random import randint


class Scene(object):

	def enter(self):
		print "This is not yet configured, Subclass it and implement enter()."
		exit(1)


class Engine(object):

	def __init__(self, scene_map):

		self.scene_map = scene_map

	def play(self):

		current_scene = self.scene_map.opening_scene()

		last_scene = self.scene_map.next_scene('finished')

		while current_scene != last_scene:

			next_scene_name = current_scene.enter()

			current_scene = self.scene_map.next_scene(next_scene_name)

		# be sure to print out the last scene
		print last_scene
		current_scene.enter()

class Death(Scene):

	quips = [
		"You diesd. You kinda suck at this.",
		"Your mom would be proud...if she were smarter.",
		"Such a luser.",
		"I have a small puppy that is better at this."
	]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)


class CentralCorridor(Scene):

	def enter(self):
		print """
		The Gothons of Planet Percal #25 have invaded your ship and destroyed
		your entire crew. You are last surviving member and your last
		mission is to get the neutron destruct bomb fro the Weapon Armory,
		put it in the bridge, and blow the ship up after getting into an
		escape pod.
		You're running down the central corridor to the Weapon Armory when
		a Gothon jumps out, red scaly skin, dark grimy teath, and evil clown costume
		flowing aroud his hate filled body. He is blocking the door to the
		Armory and about to pull a weapon to blast you.
		"""

		action = raw_input("shoot!/dodge!/tell a joke!> ")

		if action == "shoot!":
			print "Quick on the door you yank outyour blaster abd fire it at the Gothon."
			print "HIs clown costume flowing and moving around his body, which throws"
			print "off your aim. Your laser hits his costume but misses him entirely. Tthen"
			print "completly ruins his brand new costumehis mother bought him, which"
			print "makes him fly into an insane rage and blast you repeatedly in the face"
			print "you are dead. Then he eats you."

			return 'death'

		elif action == "dodge!":
			print """
		Like a world class boxer you dodge, wave, slip and slide right
		as Gothon's blaster cranks laser past your head.
		In the middle of your artful dodge your foot slips and you
		bang your head on the metal wall and pass out.
		You wake up shortly after only to die as the Gothon stomps on your head and eats you.
		"""
			return 'death'

		elif action == "tell a joke":
			print """
		Lucky for you they made you learn Gothon insults in the academy.
		You tell one Gothon joke you know:
		Lbhe zbgure fb sng, jure fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq
		The Gothon stops, tries to not laugh, then bursts out laughing and can't stop.
		While he's laughing you run up and shoot him squre in the head
		putting him down, then jump through the Weapon Armory door,
		laser_weapon_armory
		"""

		else:
			print "DOES NOT COMPUTE!"
			return 'centra_corridor'

class LaserWeaponArmory(Scene):

	def enter(self):
		print """
		You do a dive roll into the Weapon Armory. crouch and scan the room
		for more Gothons that might be hiding. It's dead quiet, too quiet.
		Your stand up and run the the far side of the room, and find the
		nuetron bombin its container. There's keypad lock on the box
		and you need the code to get the bomb out. If you get the code
		wrong 10 times then the lock closes forever and you can't
		get the bomb. The code is 3 didgits.
		"""
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[keypad]> ")
		guesses = 0

		while guess != code and guesses < 10:
			print "BZZZZEDDD!"
			guesses += 1
			guess = raw_input("[keypad]> ")

		if guess == code:
			print """
		The container clicks open and seal breaks, letting gas out.
		You grab the neutron bomb and run as fast as you can to the bridge
		where you must place itin the right spot.
		"""
			return 'the_bridege'

		else:
			print """
		The lock buzzes one last time and you hear sickening
		melting sound as the mechanism is fused togather.
		You decide to sit there, and finally the Gothons blow up the
		ship  from the shio and you die
		"""
			return 'death'

class TheBridge(Scene):

	def enter(self):

		print """
		You burst onto the Bridege wit the netron destruct bomb
		under your arm and surprise 5 Gothons who are trying to
		take of the ship. Each of the has an evel uglier
		clown costume than the last. They haven't pulled their
		weapon put yet, as they see active bomb under your
		arm and don't want to set it off.
		"""

		action = raw_input("> ")

		if action == "throw the bomb":
			print "In a panic you throw the bomb at the group of Gothons,"
			print "and make a leap for the door. Right as you drop in a"
			print "Gothon shotts you right in the back killing you."
			print "As you die you see another Gothon tries to disarm"
			print "the bomb. You die knowning they will probably blow up when"
			print "it goes off."
			return "death"

		elif action == "slowly place the bomp":
			print """
			You point your blaster at the bomb under your arm
			and Gothons puts their hands up start to sweat.
			You inch backwards to the door, open it, and then carefully
			place the bomb on the floor, pointing your blaster at it.
			You then jump bckthrought eh door, punch the close button
			and bast the lock so the Gothons can't get out.
			Now that the bomb is placed you run to escape the pod to
			get off this tin can.
			"""
			return 'escape_pod'
		else:
			print "DOES NOT COMPUTE"
			print "the_bridge"


class EscapePod(Scene):

	def enter(self):
		print """
		You rush through the ship desperately trying to make it to
		the escape pod before the whole ship explodes. It seems like
		hardly any Gothon are on the ship, so your run is clear of
		interface. You get the chabmer with the escape pods, and
		now need to pick one to take. Some of them could be damaged
		but you don't have time to look. There's 5 pods, which one
		do you take?
		"""

		good_pod = randint(1,5)
		guess = raw_init("[pod #]> ")

		if int(guess) != good_pod:
			print "you jum into pod %s and hit the eject button." % guess
			print "The pod escape out into the void of space, then"
			print "implodes as the hull ruptures, crushing your body"
			print "into jam jelly."
			return 'death'
		else:
			print "You jump into pod %s and hit the eject botton." % guess
			print "The pod easily slides out into space heading to"
			print "the planet below. As it flies to the planet, you look"
			print "back and see your ship implode than explode like a"
			print "bright star, taking out the Gothon ship at the same"
			print "time. You won!"
			return 'finished'


class Finished(Scene):

	def enter(self):
		print "You won! Good job."
		return 'finished'


class Map(object):

	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'finished': Finished(),
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
