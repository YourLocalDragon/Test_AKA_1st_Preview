import random
import time

directions = ("north", "east", "south", "west", "n", "e", "s", "w")


class Story():
    def __init__(self):
        print("This is Sparta!")


class Character():
   def __init__(self, C_health, C_attack, C_luck, C_defense, C_ranged, C_mana, C_stamina, C_name):
     self.health = C_health 
     self.attack = C_attack
     self.luck = C_luck
     self.defense = C_defense
     self.ranged = C_ranged
     self.mana = C_mana
     self.stamina = C_stamina
     self.name = C_name

   def getHealth(self):
    return self.health

   def getAttack(self):
    return self.attack

   def getLuck(self):
    return self.luck

   def getDefense(self):
    return self.defense

   def getRanged(self):
    return self.ranged

   def getMana(self):
    return self.mana

   def getStamina(self):
    return self.stamina

   def getName(self):
    return self.name

     
   def setHealth(self, new_value):
     self.health = new_value

   def setAttack(self, new_value):
     self.attack = new_value

   def setLuck(self, new_value):
     self.luck = new_value

   def setDefense(self, new_value):
     self.defense = new_value

   def setRanged(self, new_value):
     self.ranged = new_value

   def setMana(self, new_value):
     self.mana = new_value

   def setStamina(self, new_value):
     self.stamina = new_value

   def setName(self, new_value):
     self.name = new_value
     
     


class StoryTeller():
    def __init__(self):
        print("The living has no place here!\n")
        self.new_game()

    def validate_input(self, question, answers):
        answer = " "

        while answer not in answers:
            print("Invalid Input!\n")
            answer = input(question).lower()

        return answer

    def new_game(self):
        self.create_character()

    def create_character(self):
        pc_name = input(
            "Before you enter here, you must give me your name: \n-> ")
        pc_name = Character(pc_name)
        self.Introduction()

    def Introduction(self):
        print("\nNo living thing can enter this domain,")
        print("You must first give me your voice")
        print("Or you must never come near here again\n")

        pc_input = self.validate_input("Dare you begin the trial? \n-> ",
                                       ["yes", "no"])

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
        print(
            "you see nothing but darkness to the north, some metal plate to the east, a wall to the south and a doorway to the west\n"
        )
        print("Where do you wish to go?\n")
        pc_input = input("Input, north,east,south,west\n->")

        if pc_input == ("north") or pc_input == ("n"):
            print("You Fell Down A pit.....")
            quit()
        elif pc_input == ("east") or pc_input == ("e"):
            print("Your soul got crushed to by the wall closeing in")
            quit()
        elif pc_input == ("south") or pc_input == ("s"):
            print(
                "You banged your head against a wall and somehow died.... Well Done ")
            quit()
        elif pc_input == ("west") or pc_input == ("w"):
            print("\nYou went though the door and came across a monster\n")
            print(
                "You have no other escape, but you see a glimps of something")
            pass

        pc_input = input(
            "theres a sword on the ground to your right, Do you grab it or fight the monster?\n->")
        print("input grab, fight")

        if pc_input == ("grab"):
            print("The monster tears you apart\n")
            quit()
        elif pc_input == ("fight"):
            print("You face off against a little slime, the slime wins....\n")
            quit()


#new_game = StoryTeller()

#what happens if player types "yes" = Create scenario
#Input another player choice to progress story "no"


def create_class():
  response = input("Are you more strategic(1) or more of a dumbass(2)?...\n -->")
  while response != "1" and response != "2":
    print("Inalid input")
    response = input("Are you more strategic(1) or more of a dumbass(2)?...\n -->")

  if response == "1":
    charAttack = 50
    charDefense = 100
    charStamina = 50
  elif response == "2":
    charAttack = 100
    charDefense = 50
    charStamina = 100

  response = input("Enter to roll the die...\n -->")
  time.sleep(0.2)
  print("rolling the dice...")
  time.sleep(0.2)
  charLuck = random.randint(0, 20)
  print(f"You have {charLuck} out of 20")

  response = input("Bow and arrow(1) or a magic user(2)?...\n -->")
  while response != "1" and response != "2":
    print("Inalid input")
    response = input("Bow and arrow(1) or a magic user(2)?...\n -->")

  if response == "1":
    charRanged = 100
    charMana = 30
  elif response == "2":
    charRanged = 50
    charMana = 100

  charName = input("What is your name?\n -->")
  print(f"Welcome {charName} !")

  return (charAttack, charDefense, charLuck, charRanged, charMana, charStamina, charName)

class_attributes = create_class()
