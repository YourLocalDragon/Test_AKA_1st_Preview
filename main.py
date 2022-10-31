import random

class Story():
  def __init__(self):
    print ("This is Sparta!")

class Character():
  def __init__(self, name, health="100", attack="20", mana="100", stamina="50"):
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
    print("Welcome to the bad place!")
    self.new_game()
   
  def new_game(self):
    self.create_character()

  def create_character(self):
    pc_name = input("Before you enter here, you must give me your name: \n-> ")
    pc = Character(pc_name)

  def outside_the_bad_place(self):
    print("You stand before the bad place. Your time has come you utter disgrace!")
    print("You are here because you are scum and must prove your worth to society.")
    print("You must travel through the bad place and destroy the evil tyrant Lorraine!")

    pc_input = input("Dare you begin the trial? \n-> ")

    if pc_input == "yes":
      pass
    else:
      pass

new_game = StoryTeller()


#what happens if player types "yes" = Create scenario
#Input another player choice to progress story "no"