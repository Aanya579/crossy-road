from turtle import *
import random
import sys
screen = Screen()
bg = Turtle()
player = Turtle()
car = Turtle()
car2 = Turtle()
screen.register_shape("car.gif")
car.shape("car.gif")
car.color("red")
car.resizemode("user")
car2.shapesize(0.00005, 0.00005)
car2.shape("car.gif")
car2.color("red")
car2.resizemode("user")
car2.shapesize(0.00005, 0.00005)
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
  global player
  pos = player.pos()
  print(pos)
  player.goto(pos[0], pos[1]+10)
def move_down():
  global player
  pos = player.pos()
  player.goto(pos[0], pos[1]-10)
def move_right():
  global player
  pos = player.pos()
  player.goto(pos[0]+10, pos[1])
def move_left():
  global player
  pos = player.pos()
  player.goto(pos[0]-10, pos[1])
  
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_down, "Down")
screen.onkey(move_up, "Up")
screen.listen()
  
def checkAABBCollision(B, A):

  return A.xcor() < B.xcor() + 180 and A.xcor() + 55 > B.xcor() and A.ycor() < B.ycor() + 90 and A.ycor() + 55 > B.ycor()
  
class storage:
  def __init__(self, x, y):
    self.objects = []
    self.x = x
    self.y = y
    
lane1 = storage(-300, 150)
lane1.objects.append(car)
lane2 = storage(200, -50)
lane2.objects.append(car)

timer = 30
score = 0
lives = 3

def  reset():
  global player, bg, has_drawn_text
  has_drawn_text = False
  player.goto(0, -100)
  global score
  score = 0
  global lives
  lives = 3
  global timer
  timer = 30
  line1.clear()
  line2.clear()
  for turtle in lane1.objects:
    turtle.ht()
    turtle.clear()
  lane1.objects = []
  car.shape("car.gif")
  car.color("red")
  car.resizemode("user")
  car.shapesize(0.00005, 0.00005)
  bg = Turtle()
  bg.left(90)
  bg.shape("road.gif")
  player = Turtle()
  player.left(90)
  screen.addshape("chicken.gif")
  player.shape("chicken.gif")
  player.shapesize(0.05, 0.05)
  player.speed(0)
  player.goto(0, -100)
  screen.onkey(move_left, "Left")
  screen.onkey(move_right, "Right")
  screen.onkey(move_down, "Down")
  screen.onkey(move_up, "Up")
  screen.listen()

print(screen.screensize())

def exit():
  screen.bye()

line1 = Turtle()
line2 = Turtle()

has_drawn_text = False

def game():
  global lives, timer, has_drawn_text, score, player
  cars = []
  while True:
    for o in lane1.objects:
      if checkAABBCollision(o, player):
        if not o in cars:
          cars.append(o)
          lives -= 1
          print("lives", lives)
    for l in lane1.objects:
      l.forward(7)
      if l.xcor() > 200:
        l.ht()
        del l
    for o in lane2.objects:
      if checkAABBCollision(o, player):
        if not o in cars:
          cars.append(o)
          lives -= 1
          print("lives", lives)
    for l in lane2.objects:
      l.forward(-7)
      if l.xcor() < -200:
        l.ht()
        del l

    timer -= 1
    score += 10

    if timer == 0:
      car = Turtle()
      car.shape("car.gif")
      car.color("red")
      car.resizemode("user")
      car.shapesize(0.00005, 0.000005)
      car.teleport(lane1.x, lane1.y)
      car2 = Turtle()
      car2.shape("car.gif")
      car2.color("red")
      car2.resizemode("user")
      car2.shapesize(0.00005, 0.000005)
      car2.teleport(lane2.x, lane2.y)
      lane1.objects.append(car)
      lane2.objects.append(car2)
      time = random.randint(30, 100)
      timer = time
      
    if lives == 0 and has_drawn_text == False:
      screen.clear()
      has_drawn_text = True
      timer = 100000000000000
      line1.penup()
      line2.penup()
      line1.goto(-50,-200)
      line2.goto(-200, -250)
      line1.pendown()
      line2.pendown()
      line1.write("Game over")
      line2.write("Would you like to play again? Press r to start again, press n to end the game.")
    screen.onkeypress(reset, "r")
    screen.onkeypress(exit, "n")

    if player.ycor() > 240:
      print("You win!")

game()