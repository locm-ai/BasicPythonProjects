# write your code here
"""
Our program should be able to display the grid at all stages of the game. Now
we’re going to write a program that allows the user to enter a string
representing the game state and correctly prints the 3x3 game grid based on
this input. We’ll also add some boundaries around the game grid.

Adding the following functionality:
    Reads a string of 9 symbols from the input and displays them to the user
in a 3x3 grid. The grid can contain only X, O and _ symbols.
    Outputs a line of dashes --------- above and below the grid, adds a pipe |
symbol to the beginning and end of each line of the grid, and adds a space
between all characters in the grid.

"""
def display_grid(one, two, three):
    print("---------")
    print(f"| {one[0]} {one[1]} {one[2]} |")
    print(f"| {two[0]} {two[1]} {two[2]} |")
    print(f"| {three[0]} {three[1]} {three[2]} |")
    print("---------")

def game_start():
    user_input = input("Enter cells: ")
    first_row = user_input[0:3]  # Slicing 1/3 of the user input for the first row
    second_row = user_input[3:6]  # Slicing 2/3 of the user input for the second row
    third_row = user_input[6:]  # Slicing 3/3 of the user input for the last row
    display_grid(first_row, second_row, third_row)


game_start()