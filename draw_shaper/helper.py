def color_cyan(string):
    return "\033[36m" + string + "\033[0m"


def color_blue(string):
    return "\033[34m" + string + "\033[0m"


def color_red(string):
    return "\033[31m" + string + "\033[0m"

star_to_draw = color_blue("*")

def draw_circle(radius):
    for y in range(-radius, radius+1):
        for x in range(-radius, radius+1):
            if x*x + y*y <= radius*radius:
                print(star_to_draw, end="")
            else:
                print(" ", end="")
        print()

def draw_square(size):
    for y in range(size):
        for x in range(size):
            print(star_to_draw, end="")
        print()

def draw_triangle(size):
    for y in range(size):
        for x in range(y+1):
            print(star_to_draw, end="")
        print()

def draw_shape(shape, sides):
    sides_display = color_cyan(str(sides))
    if shape == "square" or shape == "1":
        print("Drawing a square with " + sides_display + " sides.")
        draw_square(sides)
    elif shape == "triangle" or shape == "2":
        print("Drawing a triangle with " + sides_display + " sides.")
        draw_triangle(sides)
    elif shape == "circle" or shape == "3":
        print("Drawing a circle with " + sides_display + " sides.")
        draw_circle(sides)
    else:
        print(color_red("Shape not recognized."))

