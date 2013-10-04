import turtle
import random
import time 

wn = turtle.Screen()
wn.bgcolor('lightgreen')

turtle_numbers = input("How many turtles (max 20)?")

finish_line = turtle.Turtle()
start_line = turtle.Turtle()

finish_line.hideturtle()
finish_line.up()
finish_line.goto(150, -200)
finish_line.pendown()
finish_line.left(90)
finish_line.forward(400)
finish_line.up()

start_line.hideturtle()
start_line.up()
start_line.goto(-100, -200)
start_line.pendown()
start_line.left(90)
start_line.forward(400)
start_line.up()

class RacingTurtle(turtle.Turtle):
	def __init__(self):
		print "racing turtle created"
		turtle.Turtle.__init__(self, shape="turtle") #all racingturtles have the shape turtle
		self.name = None
		
	def jump(self, distance):
		self.forward(distance)

	def set_name(self, name):
		self.name = name
	

turtles = []

y_pos = -(turtle_numbers/2 *20)

colors = ["red", "blue", "green", "BlanchedAlmond", "BlueViolet", "chartreuse", "dark khaki", "DarkSalmon", "DodgerBlue4", "firebrick", "FloralWhite", "goldenrod", "gold", "honeydew", "HotPink", "LemonChiffon", "mint cream", "moccasin", "OldLace", "PeachPuff", "thistle"]

def set_angle_speed(): 
	turtle_angle = random.randrange(0,180)
	if turtle_angle > 90: 
		turtle_angle += 180
	turtle_speed = random.randrange(1,100)
	return turtle_angle, turtle_speed

turtle_text = turtle.Turtle()
turtle_text.hideturtle()
for sec in range(3, 0, -1):
	turtle_text.write(sec, font=("Arial", 30, "normal"))
	time.sleep(1)
	turtle_text.clear()
	
for i in range(0, turtle_numbers, 1):
	new_turtle = RacingTurtle()
	new_turtle.color(colors[i])
	new_turtle.name = colors[i]
	turtles.append(new_turtle)
	new_turtle.up()
	new_turtle.goto(-100, y_pos)
	y_pos += 20

leader_pos = 0

while leader_pos < 150: 

	for i in range(0, turtle_numbers, 1):
		angle, speed = set_angle_speed()
		turtles[i].setheading(angle)
	for i in range(0, turtle_numbers, 1):
		angle, speed = set_angle_speed()
		turtles[i].forward(speed)
	for i in range(0, turtle_numbers, 1):
		if turtles[i].position()[0] > leader_pos:
			leader_pos = turtles[i].position()[0]
			leader = turtles[i]

turtle_text.write(leader.name + " won!", font=("Arial", 30, "normal"))

print leader.name, " won!" 


wn.exitonclick()