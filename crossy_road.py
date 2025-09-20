from turtle import *
import random
import sys
screen = Screen()
bg = Turtle()
player = Turtle()
car = Turtle()
screen.register_shape("car.gif")
car.shape("car.gif")
car.color("red")
car.resizemode("user")
car.shapesize(0.00005, 0.00005)
bg.left(90)
screen.register_shape("road.gif")
bg.shape("road.gif")
player.left(90)
screen.addshape("chicken.gif")
player.shape("chicken.gif")
player.shapesize(0.05, 0.05)
player.speed(0)
player.goto(0, -100)
def move_up():
  pos = player.pos()
  player.goto(pos[0], pos[1]+10)
def move_down():
  pos = player.pos()
  player.goto(pos[0], pos[1]-10)
def move_right():
  pos = player.pos()
  player.goto(pos[0]+10, pos[1])
def move_left():
  pos = player.pos()
  player.goto(pos[0]-10, pos[1])
  
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_down, "Down")
screen.onkey(move_up, "Up")
screen.listen()
  
def checkAABBCollision(A, B):

  AisToTheRightOfB = A.position()[0] - 30 > B.position()[0] - 30
  AisToTheLeftOfB = A.position()[0] + 30 < B.position()[0] + 30
  AisAboveB = A.position()[1] - 30 < B.position()[1] - 30
  AisBelowB = A.position()[1] + 30 > B.position()[1] + 30
  return not (AisToTheRightOfB or AisToTheLeftOfB or AisAboveB or AisBelowB);
  
class storage:
  def __init__(self, x, y):
    self.objects = []
    self.x = -300
    self.y = 150
    
lane1 = storage(0, 0)
lane1.objects.append(car)

timer = 30
score = 0
lives = 3

def  reset():
  player.goto(0, -100)
  global score
  score = 0
  global lives
  lives = 3
  global timer
  timer = 30

line1 = Turtle()
line2 = Turtle()

while True:
  for o in lane1.objects:
    if checkAABBCollision(o, player):
      lives -= 1
      print("lives", lives)
  for l in lane1.objects:
    l.forward(7)
  timer -= 1
  score += 10
  print(score)
  if timer == 0:
    car = Turtle()
    car.shape("car.gif")
    car.color("red")
    car.resizemode("user")
    car.shapesize(0.00005, 0.000005)
    car.teleport(lane1.x, lane1.y)
    lane1.objects.append(car)
    time = random.randint(30, 100)
    timer = time
    lives -= 1
  if lives == 0:
   timer = 100000000000000
   line1.write("Game over")
   line2.write("Would you like to play again? Press r to start again, press n to end the game.")
  screen.onkeypress(reset, "r")
  screen.onkeypress(sys.exit, "n")