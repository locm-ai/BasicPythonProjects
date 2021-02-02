"""
Our game is almost ready! Now let's combine what we’ve learned in the previous
stages to make a game of tic-tac-toe that two players can play from the
beginning (with an empty grid) through to the end (until there is a draw, or
one of the players wins).
The first player has to play as X and their opponent plays as O.


In this stage, we will write a program that:
    Prints an empty grid at the beginning of the game.
    Creates a game loop where the program asks the user to enter the cell
coordinates, analyzes the move for correctness and shows a grid with the
changes if everything is okay.
    Ends the game when someone wins or there is a draw.
    You need to output the final result at the end of the game.
"""


def horizantal_win(grid):
    one = grid[0:3]
    two = grid[3:6]
    three = grid[6:]
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


def vertical_win(grid):
    one = grid[0:3]
    two = grid[3:6]
    three = grid[6:]
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


def diagonal_win(grid):
    one = grid[0:3]
    two = grid[3:6]
    three = grid[6:]
    if two[1] == 'X' or two[1] == 'O':
        if one[0] == two[1] and one[0] == three[2]:
            return f"{two[1]} wins"
        elif one[2] == two[1] and one[2] == three[0]:
            return f"{two[1]} wins"


def draw(grid):
    one = grid[0:3]
    two = grid[3:6]
    three = grid[6:]
    rows = [one, two, three]
    full = True
    for row in rows:
        if '_' in row or ' ' in row:
            full = False
    if full:
        return "Draw"


"""
def count_difference(one, two, three):
    all_rows = one + two + three
    difference = max(all_rows.count('X'), all_rows.count('O')) - min(all_rows.count('X'), all_rows.count('O'))
    if difference >= 2:
        return "Impossible"
"""


def game_state(grid):  # Void function for checking win conditions
    if horizantal_win(grid) is not None:
        return horizantal_win(grid)
    elif vertical_win(grid) is not None:
        return vertical_win(grid)
    elif diagonal_win(grid) is not None:
        return diagonal_win(grid)
    elif draw(grid) is not None:
        return draw(grid)


def display_grid(grid):
    one = grid[0:3]
    two = grid[3:6]
    three = grid[6:]
    print("---------")
    print(f"| {one[0]} {one[1]} {one[2]} |")
    print(f"| {two[0]} {two[1]} {two[2]} |")
    print(f"| {three[0]} {three[1]} {three[2]} |")
    print("---------")


def play_game(user_input, resume, next_move='X'):
    if resume:
        if any([user_input.count('X') == 0,user_input.count('X') <= user_input.count('O')]):
            next_move = 'X'
        else:
            next_move = 'O'
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
                        new_input.append(next_move)
                    else:
                        new_input.append(user_input[i])
                user_input = ''.join(new_input)
                display_grid(user_input)
                if game_state(user_input) is not None:
                    print(game_state(user_input))
                else:
                    play_game(user_input, True, next_move)


def game_start(user_input="         "):
    display_grid(user_input)
    play_game(user_input, True)


game_start()
