from adventurelib import *

@when("shout loudly")
@when("shout")
@when("exclaim")
def yell():
  print("You bellow at the top of your lungs.")

@when("take THING")
def take(thing):
  print(f"You take the {thing}.")

def check_context(func):
  def inner():
    if get_context() == 'cave':
      func()
    else:
      print("You can't do that here.")
  return inner

@when("look around")
def look_around():
  print("You find yourself in a dark, damp cave.")

@when("enter the cave")
def enter_cave():
  set_context('cave')
  print("You find yourself in a cave. There is an old man sitting next to a tunnel that leads deeper.")

@when("talk to the old man")
def talk_oldman():
  set_context('cave')
  print("Young traveler, you mustn't travel here. It is too dangerous.")

@when("enter the house")
def enter_house():
  set_context('house')
  print("You find yourself in an old, abandoned house. There is a sword on the ground. Sitting next to the sword is an old lady.")

@when("talk to the old lady")
def talk_oldlady():
  set_context('house')
  print("Take this sword youngling, it may prove to become useful in time.")

@when("exit the house")
def exit_house():
  set_context('house')
  print("You exit the house.")

@when("enter the forest")
def enter_forest():
  set_context('forest')
  print("You find yourself in an ancient forest. There is a stick on the ground.")

@when("take the stick")
def take_stick():
  set_context('forest')
  print("You bend down to pick up the stick, but when you look up the forest around you starts to shift. Suddenly, you find yourself in a maze. You have two paths: left or right.")

@when("take the left path")
def take_left():
  set_context('forest')
  print("You take the left path and find yourself at a dead end.")

@when("turn back")
def turn_back():
  set_context('forest')
  print("You turn back and find yourself in the same spot as you begun.")

@when("take the right path")
def take_right():
  set_context('forest')
  print("You take the right path and you eventually find yourself out of the maze.")

sword = Item('a rusted sword', 'sword') 
sword.def_name = 'the sword'

# @when('take sword')
# def take_item(sword):
#     obj = current_room.items.take_sword
#     if not obj:
#          print(f'There is no sword here.')
#     else:
#          print(f'You take {sword.def_name}.')
#          inventory.add(obj)

start()

# 1. Test the program. What sorts of things can you type into the console, and what sorts of responses do you get? You can type get responses based on what you type, like you can type "shout" and get "You bellow at the top of your lungs."

# 2. Can you change the response you get for one of the commands you can type into the console? Yes. 

# 3. What happens when you type something there are no coded instructions for? It says "I don't understand <insert what you typed>".

# 4. Can you add a set of coded instructions for the command "look around"? I'm not sure. 