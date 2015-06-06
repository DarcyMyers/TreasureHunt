from sys import exit
from random import randint

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

        # be sure to print out the last scene
        current_scene.enter()

class Medical(Scene):

    ouch = [
        "Your bright and sparkly pedicure attracts a shark who bites one of your toes.",
         "You get stung by a stingray.",
         "You get stung by a Portugese Man O' War.",
		 "You get stung by a jellyfish."
    ]

    def enter(self):
        print Medical.ouch[randint(0, len(self.ouch)-1)]
        print "You are injured and must seek medical attention."
        exit(1)

        ##  Do we want to add option for whether or not the player gets help?
        ##  If yes, ...??  Continue the game
        ##  If no, end the game, perhaps?


class Leaving(Scene):

    def enter(self):
        print "1. Turn around and walk along the beach."
        print "2. Stare out at the ocean."
        print "3  Walk into the Gulf of Mexico until you are knee deep in the water and can feel the waves."

        choice = raw_input("> ")

        if choice == "1":
            return 'navigate'
        elif choice == "3":
            return 'medical'
        else:
            exit(1)

        ##  Need to explore what we do for option 1 and 2 ... are we getting
	    ##  further away from the treasure?


class StartFacingOcean(Scene):

    def enter(self):
        print "You stand barefoot on North Padre Island sand"
        print "facing west to the Gulf of Mexico. Before you, in the sand, is a small "
        print "pink bucket with your name on it. You pick it up.  A laughing seagull "
        print "flies over your head and cackles at you, dropping one of its feathers "
        print "to the south of you."
        print "\n"
        print "Do you:"
        print "1. Catch the feather as it falls through the air and put it in your bucket."
        print "2. Wait until it falls to the sand to pick it up and put it in your bucket."
        print "3. Do not touch it because you are afraid you will contract bird flu."

        choice = raw_input("> ")

        if choice == "1" or choice == "2":
            return 'glass'
        elif choice == "3":
            return 'leaving'
        else:
            print "I don't understand that!"
            return 'start_facing_ocean'

class Glass(Scene):

     def enter(self):
        print "After getting your feather you are facing south. You decide to walk "
        print "in that direction and feel something in the sand with your foot. You "
        print "bend over and pick it up. You are holding a piece of pink beach glass "
        print "in the shape of a heart. You admire how beautiful it is. "
        print "\n"
        print "Do you:"
        print "1. Put the heart shaped beach glass in your pail."
        print "2. Throw it into the ocean."
        print "3. Drop it back onto the sand."

        choice = raw_input("> ")

        if choice == "2" or choice == "3":
            return 'leaving'
        elif choice == "1":
            return 'shovel'
        else:
            print "I don't understand that!"
            return 'glass'

class Shovel(Scene):

    def enter(self):
        print "You continue walking along the beach and you find a small pink plastic shovel."
        print "What would you like to do with the shovel?"
        print "\n"
        print "Do you:"
        print "1. Leave it."
        print "2. Start building a sand castle, and carve a moat around the castle."
        print "3. Put the shovel in the pail."

        choice = raw_input(">")

        if choice == "1" or choice == "2":
            return 'leaving'
        elif choice == "3":
            return 'key'
        else:
            print "I don't understand that!"
            return 'shovel'

class Key(Scene):

    def enter(self):
        print "As you walk down the beach, you notice a glare in the sand."
        print "At close inspection, you see that it's an old key."
        print "Quick, what do you do? \m"

        print "1. Pick it up and put it in your pink pail."
        print "2. Ignore it, keep walking."

        choice = raw_input("> ")

        if choice == "1":
            return 'treasure_chest'
        elif choice == "2":
            print "You missed the treasure. Enjoy your beach"
            return 'leaving'

        else:
            print "Wrong choice ... try again."
            return 'key'

class XMarksTheSpot(Scene):

    def enter(self):
        print "You walk further south until you see a sandcastle the ocean has almost "
        print "completely washed away.  Some seashells appear to be in the center in an unnatural "
        print "pattern, but you can barely see them."

        print "\n"
        print "Do you:"
        print "1. Investigate."
        print "2. Keep walking." # leave

        choice = raw_input(">")

        if choice == "1":
            return 'digging'
        elif choice == "2":
            return 'leaving'  # leave
        else:
            print "I don't understand that! Please try again."
            return 'xMarksTheSpot'

class Digging(Scene):
    def enter(self):
        print "The seashells are in an X pattern."

        print "\n"
        print "Do you:"
        print "1. Start digging on the X with your shovel."
        # check to see you have shovel
        print "2. Keep walking."

        choice = raw_input(">")

        if choice == "1":
            return 'hitSomething' #need to add
        elif choice == "2":
            return 'leaving'
        else:
            print "I don't understand that! Please try again."
            return 'digging'


class HitSomething(Scene):
    def enter(self):
        print "Wow!!! Your shovel just hit something hard."
        print "You dig out the object until"
        print "you unearth a small wooden treasure chest."
        print "You look at the chest and it has a lock on "
        print "the front."

        print "\n"
        print "Do you:"
        print "1. Try unlocking with a golden key." # try again message
        # check for golden key
        print "2. Keep investigating the chest." # send to heart

        choice = raw_input(">")

        if choice == "1":
            # check and make sure you have the key
            # if not ask if want to get it

            print "The golden key doesn't unlock the chest."
            return 'HitSomething' #need to add

        elif choice == "2":
            return 'investigate'
        else:
            print "I don't understand that! Please try again."
            return 'HitSomething'


class Investigate(Scene):
    def enter(self):
        print "That's interesting. You see a heart shaped indentation on the chest."
        print "It looks like the heart shaped glass you found on the beach is the same shape."

        print "\n"
        print "Do you:"
        print "1. Try fitting the glass heart into the chest." # try again message
        # check for golden key
        print "2. Try the golden key in the lock again." # send to unlock because it didn't unlock

        choice = raw_input(">")

        if choice == "2":
            # check and make sure you have the key
            # if not ask if want to get it

            print "The golden key doesn't unlock the chest."
            return 'HitSomething' #need to add

        elif choice == "2":
            return 'unlock'
        else:
            print "I don't understand that! Please try again."
            return 'HitSomething'

class Unlock(Scene):
    def enter(self):
        print "The glass heart fits in the indentation and you can't take it back out."

        print "\n"
        print "Do you:"
        print "1. Try unlocking the chest with the golden key again." # try again message
        # check for golden key
        print "2. Shake the box and give up because it won't open."


class Treasure(Scene):
    def enter(self):
        print "The treasure chest opens and it is filled with gold Spanish doubloons. "

        return 'finished'

class Navigate(Scene):

    def enter(self):
        print "-------- NAVIGATE"
        return 'finished'

class Finished(Scene):

    def enter(self):
        print "You are now rich! Congratulations!"
        return 'finished'

class Map(object):

    scenes = {
        'start_facing_ocean': StartFacingOcean(),
        'glass': Glass(),
        'shovel': Shovel(),
        'key': Key(),
        'treasure_chest': TreasureChest(),
        'leaving': Leaving(),
        'medical': Medical(),
        'finished': Finished(),
        'navigate': Navigate(),
        'digging': Digging(),

    }

    ## Need more scenes definitions ... eg., inventory, walk on beach, etc

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)



a_map = Map('start_facing_ocean')
a_game = Engine(a_map)
a_game.play()
