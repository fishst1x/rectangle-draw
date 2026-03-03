# Name: Ryan Fisher
# Date: 12-4-2025

import sys

def main():
    width = get_width() # get the width input
    height = get_height() # get the height input
    draw_top_and_bottom(width) # draw the top
    draw_sides(height,width) # draw sides
    draw_top_and_bottom(width) # draw the bottom
    
# super awesome function that gets the width    
def get_width():
    str_width = input("Enter width of rectangle: ")
    width = int(str_width)
    if width <= 1:
        print(f"error: width ( {width} ) must be > 1") # check if value is not the right size
        sys.exit(1) # exit program
    return width

# super awesome function that gets the height 
def get_height():
    str_height = input("Enter legnth of rectangle: ")
    height = int(str_height)
    if height <= 1:
        print(f"error: height ( {height} ) must be > 1") # check if value is not the right size
        sys.exit(1) # exit program
    return height 

# function that draws top and bottom. Delimiting with space (comma).
def draw_top_and_bottom(width):
    print("+","-" * (width-2),"+")

# function that draws sides
def draw_sides(height,width):
    for _ in range(height-2):
        print("|",' ' * (width-2),"|")

if __name__ == "__main__":
    main()
