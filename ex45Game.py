from sys import exit
from random import randint



user_name = raw_input("Input your name: ")
class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
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

		current_scene.enter()


class Death(Scene):

	deathmessages = [
	"Whoops. Looks like you died..."
	]

	def enter(self):
		print Death.deathmessages[randint(0, len(self.deathmessages)-1)]
		
		return 'cave_part_one'

class StartingArea(Scene):

	

	def enter(self):

		print "\n"
		print "You wake up to find yourself in a dark cave, "
		print "where all you have is a dagger, and your sanity."
		print "Everything seems distorted and you feel "
		print "an eerie sensation climbing down your spine..."
		print "You immediately have the instict to get out of there,"
		print ""
		print "but you have no idea as to how."
		print "You remember nothing but the "
		print "voice of someone, calling out to you..."
		print "'%s, %s !', the voice says" % (user_name, user_name)
		print "\n"
		print "When your head finally stops spinning, you realize that"
		print "there are two doors in front of you."
		print "\n"
		print "It's up to you, which door do you take, %s , 1 or 2 ?" % user_name
		

		door_choice = raw_input("> ")

		if door_choice == "1":

			return 'door_one'

		elif door_choice == "2":

			return 'door_two'

		else:

			print "\n"
			print "Please pick a door in the next 10 seconds to avoid certain death."
			return 'cave_part_one'

class DoorOne(Scene):

	def enter(self):

		print "\n"
		print "You enter the room to see a sword, "
		print "stuck in a stone(how cliche, who made this lame game?)."
		print "Do you take the sword out, or not?"
		print "Choose, %s . ('take the sword out', 'leave it in there')" % user_name
		print "\n"

		sword_choice = raw_input("> ")
		sword_number = randint(1, 6)

		if sword_number >= 4:

			if sword_choice == "take the sword out":

				print "\n"
				print "As soon as you remove the sword, you hear a"
				print "loud 'click'"
				print "KAABOOOOOOOOOOOM!"
				print "You blow up, splattering blood all over the walls."
				return 'death'

			elif sword_choice == "leave it in there":

				print "\n"
				print "You hear a 'Beep, Beep, Beep' Sound "
				print "'Shouldn't have taken so long to decide', a voice whispers."
				print "KAAAABOOOOOOOOOM!"
				print "You explode, and your organs fly all over the place."
				return 'death'

			else:

				print "\n"
				print "Please pick a valid action. Jeez, it's all listed down."
				print "How hard can it be? Oh My God..." 
				return 'door_one'

		else:

			if sword_choice == "take the sword out":

				print "\n"
				print "Nothing happens and you equip"
				print "the sword. Congrats!"
				return 'cave_part_two'

			elif sword_choice == "leave it in there":

				print "\n"
				print "You don't touch the sword, "
				print "and in return the gods reward"
				print "you for not being greedy."
				return 'cave_part_two'

			else:

				print "\n"
				print "Please pick a valid action. Jeez, it's all listed down."
				print "How hard can it be? Oh My God..." 
				return 'door_one'


class DoorTwo(Scene):

	def enter(self):

		print "\n"
		print "You enter the second room, and see absolutely nothing."
		print "The room, is absolutely empty"
		print "What do you do, %s , 'nothing' or 'look around' ?" % user_name
		print "\n"

		door_two_choice = raw_input("> ")
		emptyroom_number = randint(1, 6)

		if emptyroom_number >= 3:


			if door_two_choice == "nothing":

				print "\n"
				print "You do absolutely nothing, and sit"
				print "there for all eternity."
				print "You eventually starve to death, and the"
				print "vultures eat your remains."
				print "\n"
				return 'death'

			elif door_two_choice == "look around":

				print "\n"
				print "You search long and hard, and after a lot"
				print "of time, you finally see a very, very tiny"
				print "button, hidden among the walls,"
				print "camoflaged by being of the same texture and color of the walls-"
				print "Rocky Red."

				print "\n"
				print "You press the button, and not only does a secret"
				print "entrance in the floor open up,"
				print "but a shield also drops from a hatch in the ceiling"
				print "'What Luck!'"
				print "You go through the newly opened passage..."

				return 'cave_part_two'

			else:

				print "\n"
				print "That's not a door...Do you even know what a door is?"
				return 'door_two'

		else:

			if door_two_choice == "nothing":

				print "\n"
				print "You do absolutely nothing,"
				print "and sit there for all eternity,"
				print "wondering why you wasted your"
				print "horribly lame life."
				print "You even bored the game engine"
				print "to death. Just pass the room."
				return 'cave_part_two'

			elif door_two_choice == "look around":

				print "\n"
				print "You search long and hard, and after a lot"
				print "of time, you finally see a very, very tiny"
				print "button, hidden among the ceiling,"
				print "camoflaged by being of the same texture and color of the walls-"
				print "Rocky Red."

				print "\n"
				print "However, since you are incredibly short,"
				print "You fail to reach the button, and"
				print "the gods, that are watching you with"
				print "utter disgust, electrocte you with"
				print "lightning."
				return 'death'

			else:

				print "\n"
				print "That's not a door...Do you even know what a door is?"
				return 'door_two'


class DownTheHatch(Scene):

	def enter(self):

		print "\n"
		print "You enter the next room, and"
		print "You hear the startling sound of a monster growling..."
		print "You don't want to turn around, but want to at the same time."
		print "You see a giant green monster with glowing blue eyes, "
		print "ginormous wings, and"
		print "claws that look as if they could cut diamond."
		print "This creature..."
		print "IS A CTHULU!"

		print "\n"
		print "What do you do, %s , 'run to the exit', 'panic', 'sneakily move to the exit', 'attack' " % user_name
		

		cthulu_choice = raw_input ("> ")

		if cthulu_choice == "run to the exit":

			print "\n"
			print "You manage to get to the exit,"
			print "but don't manage to do it silently."
			print "Just as you are about to reach, a"
			print "claw swiftly pierces your chest, and"
			print "you fall to the ground, wailing"
			print "in pain, and you can do absolutely nothing"
			print "about it."
			return 'death'

		elif cthulu_choice == "panic":

			print "\n"
			print "Seriously how stupid are you?"
			print "You panic, flailing your arms, "
			print "you start to cry and act like a "
			print "complete sissy. So much so, that even"
			print "the Cthulu doesn't care to kill you."
			print "It just walks away in shame, disappointed"
			print "in all of humanity."
			print "Good Job! You showed an alien race just how"
			print "pathetic you are!"
			return 'cave_part_three'

		elif cthulu_choice == "sneakily move to the exit":

			print "\n"
			print "Maybe you're sneaky,"
			print "but the Cthulu is definitely"
			print "not blind."
			print "It tramples on you with its giant feet,"
			print "instantly killing you"
			return 'death'

		elif cthulu_choice == "attack":

			print "\n"
			print "You lunge at the Cthulu, your "
			print "dagger and shield in hand, and"
			print "prepare yourself for an all out attack."
			print "You stab the Cthulu in the Chest, but realize"
			print "that you missed his heart, because you"
			print "failed Biology in school."
			print "\n"
			print "THE HEART IS ON THE LEFT NOT RIGHT,"
			print "YOU IDIOT!"

			print "\n"
			print "It swats you like a fly, and for"
			print "a brief two seconds, you experience"
			print "what it is like, to truly fly,"
			print "before you hit the wall legs first and"
			print "get flattened into the first,"
			print "human pancake."
			return 'death'

		else:
			print "\n"
			print "JUST CHOOSE AN ACTION, PLEASE!"
			return 'cave_part_two'

class MultiDoorRoom(Scene):

	def enter(self):

		print "\n"
		print "An instinct tells you that this"
		print "may just be the final room,"
		print "before you can get out of this giant rock,"
		print "and go back to your pathetic life."
		
		print "\n"
		print "However, this may just prove to be the"
		print "hardest task yet. In front of you,"
		print "Are 5 doors. You hear the cry of a"
		print "Cthulu behind you, and you know that"
		print "it's coming. You have no time to insepct"
		print "the doors, and only one of them is the"
		print "right one."

		print "\n"
		print "Note: The wrong door will shock you,"
		print "and you will have only 3 tries,"
		print "as you have 100 HP and it causes"
		print "you to lose 33.34 HP each time"
		print "Good Luck! MUAHAHAAHAHAHAHAH"

		print "\n"
		print "Which door do you choose, %s , '1', '2', '3', '4' or '5' ?" % user_name

		good_door = 3
		guess = int(raw_input("[door #]> "))
		guesses = 0

		while guess != good_door and guesses < 3 :

			print "	You lose 33.333 HP!"
			guesses += 1
			guess = int(raw_input("[door #]> "))

		if guess == good_door:
			print "You enter the next room,"
			print "with no harm done to you"
			print "' '%s ! %s !' , you hear the voice again."
			return 'final_room'
		else:
			print "You lose all your HP, and"
			print "you know what that means"
			print "R.I.P"
			return 'death'

		
class Ending(Scene):

	def enter(self):

		print "\n"
		print "In this last room, there is a button."
		print "You click it, without thinking, desperate,"
		print "to get out of this place."

		print "\n"
		print "You hear the sound of the whole cave collapsing"
		print "as a voice whispers in your ear..."
		print "'Good Job!'"

		

		print "\n"
		print "%s ! %s ! Wake up!" % (user_name, user_name)
		print "'Good Job! You're late for school!' your Mom says."
		print "Well what do you know...It was all a dream..."
		print "Or was it?"
		print "--THE END--"
		
		exit(1)

class Map(object):
	scenes = {
	'cave_part_one' : StartingArea(),
	'door_one' : DoorOne(),
	'door_two' : DoorTwo(),
	'death' : Death(),
	'cave_part_two' : DownTheHatch(),
	'cave_part_three' : MultiDoorRoom(),
	'final_room' : Ending(),
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)


a_map = Map('cave_part_one')
a_game = Engine(a_map)
a_game.play()






