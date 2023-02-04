import helper

shape = "I am in the outside"

def draw_shape(shape, sides):
    sides_display = color_cyan(str(sides))
    print(shape) # print the local variable shape maybe? "square" or "triangle" or "circle" not "I am in the outside".
    if shape == "square":
        print("Drawing a square with " + sides_display + " sides.")
    elif shape == "triangle":
        print("Drawing a triangle with " + sides_display + " sides.")
    elif shape == "circle":
        print("Drawing a circle with " + sides_display + " sides.")
    else:
        print("Shape not recognized.")

def color_cyan(string):
    return "\033[36m" + string + "\033[0m"

square_side = 4
draw_shape("square", square_side) # a variable square_side and a value "square" 
draw_shape("triangle", 3)
draw_shape("circle", 5 * 0) # an expression with * operator
# print(sides_display) # not defined error
# print(string) # not defined error
# print(sides) # not defined error
print(shape) # print "I am in the outside" shadowing is over after the function is done.

# For the first question, 
# parameters vs arguments.
# parameters
# parameters are the variables in the function definition.
# So in the function definition that started with def like this are parameters,  

# arguments are the values that are passed to the function when it is called.
# So in the function call that started with the function name like this are arguments(It is being passed to function def).

# For the second question,
# You can see in the comments and the second photo

# For the third question,
# when I call `print(sides_display)` it gives me an error because sides_display is not defined (local variable get destroyed after we finished the function).
# Note: `sides_display` is inside the function `draw_shape`

# For the fourth question,
# when I call `print(sides)` it gives me an error because sides is not defined because the scope of the function(parameter) `sides` is limited to the function.`

# For the final question,
#  I think we call that `shadowing`. When a variable defined outside a function (global variable) has the same name as local variable, the local variable has the higher priority. So when we call `print(shape)` it will print the local variable `shape` not the global variable `shape`.