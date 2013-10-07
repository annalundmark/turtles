#!/usr/bin/env python

import turtle
import random
import time
import argparse

class RacingTurtle(turtle.Turtle):
	def __init__(self):
		print "racing turtle created"
		turtle.Turtle.__init__(self, shape="turtle") #all racingturtles have the shape turtle
		self.name = None
		
	def set_name(self, name):
		self.name = name
	
	def move(self):
		turtle_angle = random.randrange(0,180)
		if turtle_angle > 90:
			turtle_angle += 180
		turtle_speed = random.randrange(1,100)
		self.setheading(turtle_angle)
		self.forward(turtle_speed)


	
wn = turtle.Screen()
wn.bgcolor('lightgreen')
	
	
controlled_turtle = RacingTurtle()
controlled_turtle.color("black")
controlled_turtle.name = "You"
controlled_turtle.up()
controlled_turtle.goto(-100, 0)
	
new_turtle = turtle.Turtle()
        
def move():
    controlled_turtle.forward(100)


wn.onkey(move, "Up")
wn.listen()
	


	#for i in range(10)
		#wn.onkey(controlled_turtle.forward(100), "Up")
		#wn.listen()



wn.exitonclick()