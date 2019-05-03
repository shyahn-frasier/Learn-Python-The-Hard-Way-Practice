from sys import exit
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
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

    def enter(self):
        print("You have died and definitely made no ancestors proud.")
        exit(1)

class PsycheRoom(Scene):
    
    def enter(self):
        print(dedent("""
            You wake in an unfamiliar room. A sinking sense of unease makes its way to the forefront
            of your consciousness once you take better stock of your surroundings. There are two
            wooden doors, one with a symbol of a crab and one with a symbol of an eel, and a wall 
            to your right made of Chinese food. Guarding the gate of this wall are two anthropomorphic 
            buttplugs, snorting some cocaine. You're definitely not in Kansas anymore. Which way do 
            you go?
            """))

        action = input("> ")
        
        if action == "crab door":
            print(dedent("""
                You make your way over to the crab door, testing the door knob to see if it'll open.
                It does open partway, but it is blocked by something on the other side. Trying to look
                through the crack made by opening the door, you see torture devices lining the walls
                of this room. Blood flows all around the floor and in the center of the room, hanging
                from a rope is a Chinese man, squirming and roaring in rage. As soon as you shiver in
                fear, his head snaps towards you, his stare icy cold; it is as if he could kill you
                with a look alone. He smiles maniacally and before you can even say anything, he rushes
                towards you, somehow free of his bonds, and stabs you through the eye and out the back 
                of your head with a hook, dragging your corpse further in for whatever twisted ideas 
                he has in mind.
                """))

            return 'death'

        elif action == "eel door":
            print(dedent("""
                Tiptoeing closer to the eel door, you try to see if the door is unlocked. It does open
                and you slip inside without the buttplug guards noticing you.
                """))

            return 'illegal_entryway'

        elif action == "chinese food":
            print(dedent("""
                You make your way to check out the wall of Chinese food. Boxes stack up high enough
                not to be able to climb, and the upright bridge is made of sticky rice. You see the
                cocaine-snorting buttplug guards sitting outside, almost oblivious to your presence.
                What do you do from here?
                """))

            chinese_food_action = input("> ")

            if chinese_food_action == "sneak in":
                print(dedent("""
                    You manage to sneak past the guards and jump onto the other end of the sticky
                    rice bridge. Making your way down, you see a town in the distance, hopefully 
                    free of danger.
                    """))
                return 'town'

            elif chinese_food_action == "snort cocaine":
                print(dedent("""
                    You greet the guards very loudly and they go on alert instantly, albeit very
                    under the influence of the drug. You offer to get rid of the rest of their
                    cocaine right now by doing it so they won't get in trouble with their superior
                    officer. They look at each other, with imaginary(?) eyes, and agree to let you
                    do cocaine with them. Sitting down at the table, you realize this is some good shit
                    and start doing a line. After going crazy and doing 5 lines of coke, you feel your
                    heart palpitate at an immense speed. This isn't what you thought it was, this is
                    cut with something that you don't like. Midway through that thought, your heart
                    gives out and you slump over, dead as a doornail and foaming at the mouth. The guards
                    end up burying you in an oversized rice container so they don't get in trouble.
                    """))
                return 'death'

        else:
            print("That's not one of the options shit for brains.")
            return 'psyche_room'

class IllegalEntryway(Scene):

    def enter(self):
        print(dedent("""
            You close the eel door softly behind you as you try to adjust your eyes to the darkness. It
            seems there is some sort of liquid river running nearby you, but you can't tell what is the
            liquid with the lack of light. What you can see is the hazy shape of a door at the end of
            the hall and what appears to be a dead child, crucified to the top. This is some fucked up
            shit. What do you do?
            """))

        action = input("> ")

        if action == "door"
            print(dedent("""
                You sidle over to the door, trying not to glance at the child's corpse, apparently
                strangled before its death and cut in half, leaving only the torso up. You find that
                the door is locked with a keypad and set out to guess the passcode. The only hint you
                can find is this: 'Something that cannot be found'.
                """))
            
            keypad = 404
            guess = input("[keypad #]> ")
            
            if guess == keypad:
                print(dedent(""" 
                    The keypad glows in acceptance and opens up, engulfing you in the scent of something
                    rotten and bloody. You reel back, covering your nose so you don't puke. You see more
                    light up ahead and you enter.
                    """))
                
                return 'dungeon'
            
            else:
                print(dedent("""
                    With that guess, the keypad turns red and the walls start to vibrate. Backing up
                    quickly, to the center of the room, you see the door get ripped off its hinges as
                    a blobby monster slithers its way inside. It yells out 'THAT IS MY TRAPPERKEEPER
                    KYLE!!' and proceeds to absorb you into itself
                    """))
                
                return 'death'

class Town(Scene):

    def enter(self):
        print(dedent("""
            
            """))

class Dungeon(Scene):

    def enter(self):
        print(dedent("""
            
            """))

class Finished(Scene):

    def enter(self):
        print("You have survived. This time...")
        return 'finished'

class Map(object):

    scenes = {
        'psyche_room': PsycheRoom(),
        'illegal_entryway': IllegalEntryway(),
        'town': Town(),
        'dungeon': Dungeon(),
        'death': Death(),
        'finished': Finished(),

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('psyche_room')
a_game = Engine(a_map)
a_game.play()