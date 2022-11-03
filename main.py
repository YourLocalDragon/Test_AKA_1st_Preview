import random
directions = ("north","east","south","west","n","e","s","w")

class Story():
    def __init__(self):
        print("This is Sparta!")


class Character():
    def __init__(self,
                 name,
                 health="100",
                 attack="20",
                 mana="100",
                 stamina="50"):
        self.name = name
        self.hp = health
        self.ap = attack
        self.mp = mana
        self.stamina = stamina

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_atk(self, defense_roll):
        atk = random.randint(0, self.ap)
        print(atk)

        if atk < defense_roll:
            atk = 0
        else:
            atk -= defense_roll
        return atk

    def is_dead(self):
        if self.hp < 1:
            return True
        else:
            return False


#Print("Welcome " + pc.name)
#print(f"You Have {pc.hp} health")
#print(f"You Have {pc.ap} attack")
#print(f"You Have {pc.mp} mana")
#print(f"You Have {pc.stamina} stamina")


class StoryTeller():

  
    def __init__(self):
        print("The living has no place here!\n")
        self.new_game()

    def new_game(self):
        self.create_character()

    def create_character(self):
        pc_name = input("Before you enter here, you must give me your name: \n-> ")
        pc_name = Character(pc_name)
        self.Introduction()
        

    def Introduction(self):
        print("\nNo living thing can enter this domain,")
        print("You must first give me your voice")
        print("Or you must never come near here again\n")

        pc_input = input("Dare you begin the trial? \n-> ")

        if pc_input == "yes":
            print("\nYou stand there ready as you can be\n")
            self.Start_Game()
        else:
            print("Your are not ready for this, come back when you are")
            quit()
    
  
    def Start_Game(self):
      print("The Reaper takes you in as a soul")
      print("-----------")
      print("-----------")
      print("-----------")
      print("-----------\n")
      print("you see nothing but darkness to the north, some metal plate to the east, a wall to the south and a doorway to the west\n")
      print("Where do you wish to go?\n")
      pc_input = input("Input, north,east,south,west\n->")

      if pc_input == ("north"):
        print("You Fell Down A pit.....")
        quit()
      elif pc_input == ("east"):
        print("Your soul got crushed to by the wall closeing in")
        quit()
      elif pc_input == ("south"):
        print("You banged your head against a wall and somehow died.... Well Done ")
        quit()
      elif pc_input == ("west"):
        print("\nYou went though the door and came across a monster\n")
        print("You have no other escape, but you see a glimps of something")
        pass 
      
      pc_input = input("theres a sword on the ground to your right, Do you grab it or fight the monster?\n->")
      print("input grab, fight")

      if pc_input == ("grab"):
        print("The monster tears you apart\n")
        quit()
      elif pc_input == ("fight"):
        print("You face off against a little slime, the slime wins....\n")
        quit()
      
      
      
      



new_game = StoryTeller()

#what happens if player types "yes" = Create scenario
#Input another player choice to progress story "no"
