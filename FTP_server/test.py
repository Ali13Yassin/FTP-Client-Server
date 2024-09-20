from tkinter import Canvas
import random
import time

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300

N_CIRCLES = random.randint(5, 100)

def main():
    print('Random Circles')
    print(N_CIRCLES)
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for i in range(N_CIRCLES):
        CIRCLE_SIZE = random.randint(5, 100) # Random size of the circle
        left_x = random.randint(0, CANVAS_WIDTH-CIRCLE_SIZE) # Random x position of the circle
        top_y = random.randint(0, CANVAS_HEIGHT-CIRCLE_SIZE) # Random y position of the circle
        right_x = left_x + CIRCLE_SIZE # The width of the circle
        bottom_y = top_y + CIRCLE_SIZE # The height of the circle
        color = random_color() # Random color of the circle
        outline = random_color() 
        shape = random_shape()
        if shape == "circle":
            circle = canvas.create_oval(left_x, top_y, right_x, bottom_y, color, outline)
        elif shape == "square":
            square = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, color, outline)
        elif shape == "rectangle":
            right_x += random.randint(20, 80)
            rectangle = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, color, outline)
        elif shape == "oval":
            right_x += random.randint(20, 80)
            oval = canvas.create_oval(left_x, top_y, right_x, bottom_y, color, outline)
        time.sleep(0.05)

#Random shape function
def random_shape():
    shapes = ["circle", "square", "oval", "rectangle"]
    return random.choice(shapes)

def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

if __name__ == '__main__':
    main()