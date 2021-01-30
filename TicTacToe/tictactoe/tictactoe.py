"""
Our program should be able to display the grid at all stages of the game. Now
we’re going to write a program that allows the user to enter a string
representing the game state and correctly prints the 3x3 game grid based on
this input. We’ll also add some boundaries around the game grid.

Adding the following functionality:
    Take a string entered by the user and print the game grid as in the
    previous stage.
    Analyze the game state and print the result. Possible states:
    Game not finished when neither side has three in a row but the grid still
    has empty cells.
    Draw when no side has a three in a row and the grid has no empty cells.
    X wins when the grid has three X’s in a row.
    O wins when the grid has three O’s in a row.
    Impossible when the grid has three X’s in a row as well as three O’s in a
    row, or there are a lot more X's than O's or vice versa (the difference
    should be 1 or 0; if the difference is 2 or more, then the game state is
    impossible).

"""


def horizantal_win(one, two, three):
    counter = 0
    winning_letter = ''
    rows = [one, two, three]
    for row in rows:  # Check for horizantal win
        if row[0] == row[1] and row[0] == row[2]:
            counter += 1
            winning_letter = row[0]

    if counter == 1:
        return (f"{winning_letter} wins")
    elif counter > 1:
        return "Impossible"



def vertical_win(one, two, three):
    counter = 0
    winning_letter = ''
    for i in range(0, 3):
        if one[i] == two[i] and one[i] == three[i]:
            counter += 1
            winning_letter = one[i]
    if counter == 1:
        return (f"{winning_letter} wins")
    elif counter > 1:
        return "Impossible"


def diagonal_win(one, two, three):
    if one[0] == two[1] or one[2] == two[1]:
        if one[0] == three[2] or one[2] == three[0]:
            return (f"{two[1]} wins")

def draw(one, two, three):
    rows = [one, two, three]
    full = True
    for row in rows:
        if '_' in row or ' ' in row:
            full = False
    if full == True:
        return "Draw"

def count_difference(one, two, three):
    all_rows = one + two + three
    difference = max(all_rows.count('X'), all_rows.count('O')) - min(all_rows.count('X'), all_rows.count('O'))
    if difference >= 2:
        return "Impossible"

def game_state(one, two, three):  # Void function for checking win conditions
    if horizantal_win(one, two, three) != None:
        return (horizantal_win(one, two, three))
    elif vertical_win(one, two, three) != None:
        return (vertical_win(one, two, three))
    elif diagonal_win(one, two, three) != None:
        return (diagonal_win(one, two, three))
    elif draw(one, two, three) != None:
        return (draw(one, two, three))
    elif count_difference(one, two, three) != None:
        return (count_difference(one, two, three))
    else:
        return ("Game not finished")


def display_grid(one, two, three):
    print("---------")
    print(f"| {one[0]} {one[1]} {one[2]} |")
    print(f"| {two[0]} {two[1]} {two[2]} |")
    print(f"| {three[0]} {three[1]} {three[2]} |")
    print("---------")

def game_start(first_row = "___", second_row = "___", third_row = "___"):
    user_input = input("Enter cells: ")
    new_first_row = user_input[0:3]  # Slicing 1/3 of the user input for the first row
    new_second_row = user_input[3:6]  # Slicing 2/3 of the user input for the second row
    new_third_row = user_input[6:]  # Slicing 3/3 of the user input for the last row
    display_grid(new_first_row, new_second_row, new_third_row)
    if game_state(new_first_row, new_second_row, new_third_row) != None:
        print(game_state(new_first_row, new_second_row, new_third_row))
    else:
        game_start(new_first_row, new_second_row, new_third_row)


game_start()
