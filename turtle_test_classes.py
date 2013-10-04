import turtle
import random

wn = turtle.Screen()
wn.bgcolor('lightgreen')

class RacingTurtle(turtle.Turtle):
	def __init__(self):
		print "racing turtle created"
		turtle.Turtle.__init__(self, shape="turtle") #all racingturtles have the shape turtle
		#self.color(color)
	def jump(self, distance):
		self.forward(distance)
	
		

green_turtle = RacingTurtle()
green_turtle.jump(100)


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