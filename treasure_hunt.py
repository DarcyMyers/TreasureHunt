from sys import exit
from random import randint

inventory = set()
location = 'start_facing_ocean'

class Scene(object):

    def enter(self):
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


class Leaving(Scene):

    def enter(self):
        print "1. Turn around and walk north along the beach."
        print "2. Stare out at the ocean."
        print "3  Walk into the Gulf of Mexico until you are knee deep in the water and can feel the waves."

        choice = raw_input("> ")

        if choice == "1":
            print "So long.  Enjoy your walk!"
        elif choice == "2":
            print "Nice scenery?  See any flying fish?  Hope you like the view!"
        elif choice == "3":
            return 'medical'

        exit(1)


class StartFacingOcean(Scene):

    def enter(self):
        print "You stand barefoot on North Padre Island sand"
        print "facing west to the Gulf of Mexico. Before you, in the sand, is a small "
        print "pink pail with your name on it. You pick it up.  A laughing seagull "
        print "flies over your head and cackles at you, dropping one of its feathers "
        print "to the south of you."
        print "\n"
        print "Do you:"
        print "1. Catch the feather as it falls through the air and put it in your pail."
        print "2. Wait until it falls to the sand to pick it up and put it in your pail."
        print "3. Do not touch it because you are afraid you will contract bird flu."

        choice = raw_input("> ")

        if choice == "1" or choice == "2":
            inventory.add("feather")
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

        if choice == "2":
            return 'leaving'
        elif choice == "1":
            inventory.add("glass")
            return 'shovel'
        elif choice == "3":
            location = 'glass'
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
            location = 'shovel'
            return 'leaving'
        elif choice == "3":
            inventory.add("shovel")
            return 'key'
        else:
            print "I don't understand that!"
            return 'shovel'

class Key(Scene):

    def enter(self):
        print "As you walk down the beach, you notice a glare in the sand."
        print "At close inspection, you see that it's an old key."
        print "Quick, what do you do? \n"

        print "1. Pick it up and put it in your pink pail."
        print "2. Ignore it, keep walking."

        choice = raw_input("> ")

        if choice == "1":
            inventory.add("key")
            return 'x_marks_the_spot'
        elif choice == "2":
            location = 'key'
            print "You missed the treasure. Enjoy your beach"
            return 'leave'

        else:
            print "Wrong choice ... try again."
            return 'key'

class XMarksTheSpot(Scene):

    def enter(self):
        print "You walk further south until you see a sandcastle the ocean has almost "
        print "completely washed away.  Some seashells appear to be in the center in a "
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
            return 'x_marks_the_spot'

class Digging(Scene):
    def enter(self):
        print "The seashells are in an X pattern."

        print "\n"
        print "Do you:"
        print "1. Start digging."
        print "2. Keep walking."

        choice = raw_input(">")

        if choice == "1":
            if 'shovel' in inventory:
                return 'hit_something'
                #return 'treasure_chest'
            else:
                print "You don't have a shovel, but you went back to get the one you found earlier so that you can start digging."
                inventory.add('shovel')
                return 'hit_something'
                #return 'treasure_chest'
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
            if 'key' in inventory:
                print "\n"
                print "\n"
                print "The golden key doesn't unlock the chest."
                print "\n"
                print "\n"
                return 'hit_something' #need to add
            else:
                print "\n"
                print "\n"
                print "You don't have the key. No problem. You went back to get the key."
                print "The golden key doesn't unlock the chest."
                print "\n"
                print "\n"
                inventory.add('key')
                return 'hit_something'
        elif choice == "2":
            return 'investigate'
        else:
            print "I don't understand that! Please try again."
            return 'hit_something'


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

        if choice == "1":
            return 'unlock'

        elif choice == "2":
            if 'key' in inventory:
                print "\n"
                print "\n"
                print "Oh no! The golden key doesn't work. Do you want to try the heart?"
                print "\n"
                print "\n"
                return 'investigate'
            else:
                print "\n"
                print "\n"
                print "You don't have the key. No problem. You went back to get the key."
                print "Oh no! The golden key doesn't work. Do you want to try the heart?"
                print "\n"
                print "\n"
                inventory.add('key')
                return 'investigate'
        else:
            print "\n"
            print "\n"
            print "I don't understand that! Please try again."
            print "\n"
            print "\n"
            return 'investigate'

class Unlock(Scene):
    def enter(self):
        print "\n"
        print "\n"
        print "The glass heart fits in the indentation and you can't take it back out."
        print "\n"
        print "\n"
        print "Do you:"
        print "1. Try unlocking the chest with the golden key again." # try again message
        # check for golden key
        print "2. Shake the box and give up because it won't open."

        choice = raw_input(">")

        if choice == "1":
            print "\n"
            print "\n"
            return 'treasure_chest'
            print "\n"
            print "\n"
        elif choice == "2":
            return 'leave'
        else:
            print "\n"
            print "\n"
            print "I don't understand that! Please try again."
            print "\n"
            print "\n"
            return 'unlock'

class TreasureChest(Scene):
    def enter(self):
        print "\n"
        print "\n"
        print "The treasure chest opens and it is filled with gold Spanish doubloons. "
        print "\n"
        print "\n"
        return 'finished'


class Finished(Scene):

    def enter(self):
        print "\n"
        print "You are now rich! Congratulations!"
        return 'finished'

class Map(object):

    scenes = {
        'start_facing_ocean': StartFacingOcean(),
        'glass': Glass(),
        'shovel': Shovel(),
        'key': Key(),
        'leaving': Leaving(),
        'medical': Medical(),
        'finished': Finished(),
        'digging': Digging(),
        'investigate': Investigate(),
        'x_marks_the_spot': XMarksTheSpot(),
        'unlock': Unlock(),
        'treasure_chest': TreasureChest(),
        'hit_something': HitSomething(),
    }


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
