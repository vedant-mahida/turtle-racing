import turtle
import time
import random

# Constants 
WIDTH, HEIGHT = 850, 850
SCREEN_COLOR = "black"
TURTLE_SHAPE = "turtle"
TURTLE_COLORS = ['red', 'yellow', 'green', 'orange', 'blue', 
                'white', 'purple', 'pink', 'cyan', 'brown']

# Greetings
print(":::::::::::::: WELCOME TO THE TURTLE RACING ::::::::::::::")
print("Game will close automatically after 3 seconds after the race ends....")
print("\tBET on your turtle!")

# FUNCTION: Screen setup
def set_screen():
  screen = turtle.Screen()
  screen.setup(WIDTH, HEIGHT)
  screen.bgcolor(SCREEN_COLOR)
  screen.title("Turtle Racing")

# FUNCTION: Take user input
def get_num_of_turtles():
  turtles = 0
  while True:
    turtles = input("Enter Number Of Turtles (2-10): ")
    # Check 1: is digit ?
    if turtles.isdigit():
      turtles = int(turtles)
    else:
      print(f"{turtles} is not a numerical value...Try Again...")
      continue
    # Check 2:  is in range ?
    if 2 <= turtles <= 10:
      return turtles
    else:
      print(f"{turtles} is out of range (2 - 10)...")
      continue


# FUNCTION: Create turtles
def create_turtles(colors):
  turtles = []
  space_between_turtle = WIDTH // (len(colors) + 1)
  for i, color in enumerate(colors):
    t = turtle.Turtle()
    t.color(color)
    t.shape(TURTLE_SHAPE)
    t.left(90)
    # set turtle position
    t.penup()
    turtleXpos = -WIDTH // 2 + (i+1) * space_between_turtle # on -x axis
    turtleYpos = -HEIGHT // 2 + 20 # on -y axis
    t.setpos(turtleXpos, turtleYpos)
    t.pendown()
    turtles.append(t)
  return turtles


# FUNCTION: Start Race
def race(colors):
  turtles = create_turtles(colors)
  while True:
    for t in turtles:
      move_distance = random.randrange(1, 20)
      t.forward(move_distance)
      x_distane, y_distance = t.pos()
      if y_distance >= HEIGHT // 2 - 25:  # finish line, 25 offset y-axis
        return colors[turtles.index(t)]


racers = get_num_of_turtles()
set_screen()

random.shuffle(TURTLE_COLORS) # random color racer everytime
colors = TURTLE_COLORS[:racers]  # ex. 3 racers => [0:3] => [3 random colors]

winner = race(colors)
print(f"{winner.upper()} racer is the winner!")
time.sleep(3)

