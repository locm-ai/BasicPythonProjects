"""
    It’s time to make our game interactive! Now we’re going to add the ability
for a user to make a move. To do this, we need to divide the grid into cells.
Suppose the top left cell has the coordinates (1, 1) and the bottom right cell
has the coordinates (3, 3) like in this table:
    (1, 1) (1, 2) (1, 3)
    (2, 1) (2, 2) (2, 3)
    (3, 1) (3, 2) (3, 3)
    The program should ask the user to enter the coordinates of the cell where
they want to make a move. In this stage, the user plays as X, not O. Keep in
mind that the first coordinate goes from left to right and the second
coordinate goes from top to bottom. Also note that coordinates start with 1
and can be 1, 2, or 3. What happens if the user enters incorrect coordinates?
The user could enter symbols instead of numbers, or enter coordinates
representing occupied cells or cells that aren’t even on the grid. You need to
check the user's input and catch possible exceptions.


Adding the following functionality:
    Get the 3x3 grid from the input as in the previous stages.
    Output this 3x3 grid as in the previous stages.
    Prompt the user to make a move.
    The user should input 2 numbers that represent the cell where they want to
place their X. (the 9 symbols representing the field will be the first line of
input, and the 2 coordinate numbers will be the second line of input)
    Analyze user input and show messages in the following situations: This
cell is occupied! Choose another one! if the cell is not empty. You should
enter numbers! if the user enters non-numeric symbols in the coordinates
input. Coordinates should be from 1 to 3! if the user enters coordinates
outside the game grid.
    Update the grid to include the user's move and print the updated grid to
    the console.
"""


def horizantal_win(one, two, three):
    counter = 0
    winning_letter = ''
    rows = [one, two, three]
    for row in rows:  # Check for horizantal win
        if row[0] == 'X' or row[0] == 'O':
            if row[0] == row[1] and row[0] == row[2]:
                counter += 1
                winning_letter = row[0]
    if counter == 1:
        return f"{winning_letter} wins"
    elif counter > 1:
        return "Impossible"


def vertical_win(one, two, three):
    counter = 0
    winning_letter = ''
    for i in range(0, 3):
        if one[i] == 'X' or one[i] == 'O':
            if one[i] == two[i] and one[i] == three[i]:
                counter += 1
                winning_letter = one[i]
    if counter == 1:
        return f"{winning_letter} wins"
    elif counter > 1:
        return "Impossible"


def diagonal_win(one, two, three):
    if two[1] == 'X' or two[1] == 'O':
        if one[0] == two[1] and one[0] == three[2]:
            return f"{two[1]} wins"
        elif one[2] == two[1] and one[2] == three[0]:
            return f"{two[1]} wins"


def draw(one, two, three):
    rows = [one, two, three]
    full = True
    for row in rows:
        if '_' in row or ' ' in row:
            full = False
    if full == True:
        return "Draw"

"""
def count_difference(one, two, three):
    all_rows = one + two + three
    difference = max(all_rows.count('X'), all_rows.count('O')) - min(all_rows.count('X'), all_rows.count('O'))
    if difference >= 2:
        return "Impossible"
"""

def game_state(one, two, three):  # Void function for checking win conditions
    if horizantal_win(one, two, three) != None:
        return (horizantal_win(one, two, three))
    elif vertical_win(one, two, three) != None:
        return (vertical_win(one, two, three))
    elif diagonal_win(one, two, three) != None:
        return (diagonal_win(one, two, three))
    elif draw(one, two, three) != None:
        return (draw(one, two, three))
    """
    elif count_difference(one, two, three) != None:
        return (count_difference(one, two, three))
    else:
        return ("Game not finished")
    """

def display_grid(grid):
    one = grid[0:3]
    two = grid[3:6]
    three = grid[6:]
    print("---------")
    print(f"| {one[0]} {one[1]} {one[2]} |")
    print(f"| {two[0]} {two[1]} {two[2]} |")
    print(f"| {three[0]} {three[1]} {three[2]} |")
    print("---------")


def play_game(user_input, resume = True):
    if resume:
        input_coordinate = input("Enter the coordinates: ").split()
        if input_coordinate[0].isalpha():
            print("You should enter numbers!")
            play_game(user_input, True)
        elif int(input_coordinate[0]) < 1 or int(input_coordinate[0]) > 3:
            print("Coordinates should be from 1 to 3!")
            play_game(user_input, True)
        elif int(input_coordinate[1]) < 1 or int(input_coordinate[1]) > 3:
            print("Coordinates should be from 1 to 3!")
            play_game(user_input, True)
        else:
            formatted_coordinates = ((int(input_coordinate[0]) - 1) * 3) + (int(input_coordinate[1]) - 1)
            if user_input[formatted_coordinates] == 'X' or user_input[formatted_coordinates] == 'O':
                print("The cell is occupied! Choose another one!")
                play_game(user_input, True)
            else:
                new_input = []
                for i in range(len(user_input)):
                    if i == formatted_coordinates:
                        new_input.append('X')
                    else:
                        new_input.append(user_input[i])
                user_input = ''.join(new_input)
                display_grid(user_input)
                play_game(user_input, False)

def game_start():
    user_input = input("Enter cells: ")
    display_grid(user_input)
    play_game(user_input)


game_start()
