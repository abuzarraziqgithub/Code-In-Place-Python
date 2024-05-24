
#* Section 5: Graphics

#* In this section, our goal is to work on a graphics problem together.

#? Problem: Random Circles

#? Write a program that draws a 20 circles at random positions with random colors on the canvas. You are provided with the constants N_CIRCLES (the number of circles to draw), CANVAS_WIDTH and CANVAS_HEIGHT (the width and height of the canvas, respectively) and CIRCLE_SIZE (the width and height of each circle respectively). Specifically, your job is to implement the following function:

#* def draw_random_circle(canvas):

#* which takes as a parameter the canvas that will be used to draw all of the random circles. In order to choose a random color, we have a defined a function for you to use called random_color(). It will return a random color that you can use for a given circle. 

# def random_color():
#     colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
#     return random.choice(colors)


#* Making all the necessary calls to your draw_random_circle(...) function should produce something that looks like this (of course with randomness yours will have the circles in different locations:

#* Possible Extensions:

#? If you find you have extra time you can try adding the following extensions on to this problem

#* Draw a random number of circles between 1 and 20

#* Draw circles of a random size 

#* Draw the circles such that all parts of the circle are within the canvas 




import random
import tkinter as tk

# Constants
N_CIRCLES = 20
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
CIRCLE_SIZE = 50

def random_color():
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

def draw_random_circle(canvas):
    for _ in range(N_CIRCLES):
        # Generate random size for the circle
        circle_size = random.randint(20, CIRCLE_SIZE)

        # Generate random position, ensuring the circle fits within the canvas
        x0 = random.randint(0, CANVAS_WIDTH - circle_size)
        y0 = random.randint(0, CANVAS_HEIGHT - circle_size)
        x1 = x0 + circle_size
        y1 = y0 + circle_size

        # Get random color
        color = random_color()

        # Draw the circle on the canvas
        canvas.create_oval(x0, y0, x1, y1, fill=color, outline=color)

# Create the Tkinter window and canvas
window = tk.Tk()
canvas = tk.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

# Draw the random circles
draw_random_circle(canvas)

# Run the Tkinter event loop
window.mainloop()
