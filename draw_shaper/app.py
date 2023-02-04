import helper;
def start():
    print("\n1. Draw a square")
    print("2. Draw a triangle")
    print("3. Draw a circle ")
    print("4. Exit \n")
    user_choice_shape = input("Enter the shape that you want to draw(name or number): ")
    if(user_choice_shape == "4"):
        return
    user_choice_sides = input("Enter the number of sides: ")
    
    helper.draw_shape(user_choice_shape, int(user_choice_sides))
    start()

