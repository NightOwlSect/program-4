import turtle
import random

# Set up the screen window
window = turtle.Screen()

# Create a visible turtle object
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.shapesize(4)
my_turtle.color("purple")
my_turtle.pendown()

def click_handler(x=0, y=0):
    colors = ["#FF5733", "#33FF57", "#ddff33", "#3357FF", "#F333FF", "#33FFF5"]
    my_turtle.color(random.choice(colors))
    my_turtle.right(20)
    my_turtle.forward(50)
    window.ontimer(click_handler,500)


my_turtle.onclick(click_handler)

# Keep the window open and listening for events
window.mainloop()
