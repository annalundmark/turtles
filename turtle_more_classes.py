import turtle
import random
import time
import argparse

def main(debug):

	wn = turtle.Screen()
	wn.bgcolor('lightgreen')

	turtle_numbers = input("How many turtles (max 20)?")


	class RacingTurtle(turtle.Turtle):
		def __init__(self):
			print "racing turtle created"
			turtle.Turtle.__init__(self, shape="turtle") #all racingturtles have the shape turtle
			self.name = None

		def set_name(self, name):
			self.name = name
		
		def set_angle(self):
			turtle_angle = random.randrange(0,180)
			if turtle_angle > 90:
				turtle_angle += 180
			return turtle_angle
		
		def set_speed(self):
			turtle_speed = random.randrange(1,100)
			return turtle_speed
		
	
	
	turtles = []
	
	y_pos = -(turtle_numbers/2 *20)
	
	colors = ["red", "blue", "green", "BlanchedAlmond", "BlueViolet", "chartreuse", "dark khaki", "DarkSalmon", "DodgerBlue4", "firebrick", "FloralWhite", "goldenrod", "gold", "honeydew", "HotPink", "LemonChiffon", "mint cream", "moccasin", "OldLace", "PeachPuff", "thistle"]
	

	turtle_text = turtle.Turtle()
	turtle_text.hideturtle()
	turtle_text.write('ready ...', font=("Arial", 30, "normal"))
	
		
	for i in range(0, turtle_numbers, 1):
		new_turtle = RacingTurtle()
		new_turtle.color(colors[i])
		new_turtle.name = colors[i]
		turtles.append(new_turtle)
		new_turtle.up()
		new_turtle.goto(-100, y_pos)
		y_pos += 20
	
	turtle_text.hideturtle()
	turtle_text.clear()
	secs = range(3, 0, -1)
	secs.append('go!!')
	for sec in secs:
		turtle_text.write(sec, font=("Arial", 30, "normal"))
		time.sleep(1)
		turtle_text.clear()
	
	leader_pos = 0

	while leader_pos < 150: 
	
		i = random.randrange(0, turtle_numbers)
		turtles[i].setheading(turtles[i].set_angle())
		turtles[i].forward(turtles[i].set_speed())
		if turtles[i].position()[0] > leader_pos:
			leader_pos = turtles[i].position()[0]
			leader = turtles[i]
	
	turtle_text.write(leader.name + " won!", font=("Arial", 30, "normal"))

	print leader.name, " won!" 

	wn.exitonclick()

if __name__ == "__main__": 
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument('-d', '--debug', action='store_true', default=False, help='Debug mode')

	args = parser.parse_args()
	main(args.debug)