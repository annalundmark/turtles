import turtle
import random

wn = turtle.Screen()
wn.bgcolor('lightgreen')

turtle_numbers = input("How many turtles?")

class RacingTurtle(turtle.Turtle):
	def __init__(self):
		print "racing turtle created"
		turtle.Turtle.__init__(self, shape="turtle") #all racingturtles have the shape turtle
		#self.color(color)
	def jump(self, distance):
		self.forward(distance)

turtles = []

y_pos = 0

colors = ["red", "blue", "green"]
	
for i in range(0, turtle_numbers, 1):
	new_turtle = RacingTurtle()
	new_turtle.color(colors[i])
	turtles.append(new_turtle)
	new_turtle.goto(-100, y_pos)
	y_pos += 20

for i in range(0, turtle_numbers, 1):
	turtles[i].jump(100)
#green_turtle = RacingTurtle()
#green_turtle.color("green")
#green_turtle.jump(100)


#red_turtle = turtle.Turtle()
#blue_turtle = turtle.Turtle()
#red_turtle.color('red')
#blue_turtle.color('blue')
#red_turtle.shape('turtle')
#blue_turtle.shape('turtle')


#blue_turtle.up()
#red_turtle.up()
#blue_turtle.goto(-100,20)
#red_turtle.goto(-100,-20)



wn.exitonclick()