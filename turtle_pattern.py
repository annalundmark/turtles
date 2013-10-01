import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('blue')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('white')
andy.shape('turtle')
lance.shape('turtle')

'''Comment added to test out branching'''

distance = input("distance between turtles: ")

andy.up()

def float_range(min, max, distance): 
	current = min
	while current < max: 
		yield current
		current += distance
		
floatRange = float_range(5,200,distance)

for size in floatRange:
    andy.stamp()
    andy.forward(size)
    andy.right(24) 

lance.up()

for size in float_range(5,200,distance*2):
    lance.stamp()
    lance.forward(size)
    lance.right(24)

wn.exitonclick()