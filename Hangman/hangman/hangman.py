'''
Take on the popular game Hangman
Eventually will include the following aspects
    In the main menu, a player can choose to either play or exit the game.
    If the user chooses to play, the computer picks a word from a list: this will be the answer to the puzzle.
    The computer asks the player to enter a letter that they think is in the word.
    If that letter does not appear in the word and this letter hasn't already been guessed, the computer counts it as a miss. A player can only afford 8 misses before the game is over.
    If the letter does occur in the word, the computer notifies the player. If there are letters left to guess, the computer invites the player to go on.
    When the entire word is uncovered, it's a victory! The game calculates the final score and returns to the main menu.

Adding the following functionality
    Ask the player for a possible word.
    Print You survived! if the user guesses the word.
    Print You lost! if the user guesses incorrectly.
'''

print("H A N G M A N")
hidden_word = "python" #placeholder word
guess = input("Guess the word: ") # Prompts user for a guess and stores as a string
if guess == hidden_word:  # Checks if the users guess matches with the word and outputs a win/loss statement
    print("You survived!")
else:
    print("You lost!")