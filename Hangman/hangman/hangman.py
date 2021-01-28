# Write your code here
import random
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
    Print That letter does not appear in the word and reduce the number of remaining attempts if the word selected by the program doesn't contain this letter.
    Print No improvements and reduce the attempts count if the selected word contains this letter but the user has already tried guessing it.
    The number of remaining attempts should be decreased only if there are no letters to uncover.

'''

print("H A N G M A N")
hidden_words = ['python', 'java', 'kotlin', 'javascript']
hidden_word = hidden_words[random.randint(0, len(hidden_words) - 1)]  # picks a random word
word_display = ("-" * (len(hidden_word)))  # formats the word to provide a hint
remaining_attempts = 8
guessed_letters = []
while remaining_attempts > 0:  # Looping structure until user is out of attempts
    print()
    print(f"{word_display}")  # display the word, hidden by "-"
    guess = input("Input a letter: ")  # Prompts user for a guess(with hint provided) and stores as a string
    if guess in hidden_word and guess in guessed_letters:
        print("No improvements")
        remaining_attempts -= 1  # lowers remaining attempts
    elif guess not in hidden_word:  # checks if the users guess is a part of the hidden_word and outputs message if it is not
        print("That letter doesn't appear in the word")
        remaining_attempts -= 1  # lowers remaining attempts
    guessed_letters.append(guess)  # adds guess to list of guessed_letters
    temp_display = hidden_word  # copy of hidden_word
    for letters in hidden_word:  # parses through every character in hidden_word
         if letters not in guessed_letters:  # boolean check if a character in hidden_word is a part of guessed_letters
             temp_display = temp_display.replace(letters, "-")  #replaces every character that fulfils the above requirements with "-"
    word_display = temp_display  # overwrite what is display at the start of the loop
    if word_display == hidden_word:
        break
    # print("\n")  # new line for formatting
if word_display == hidden_word:
    print(word_display)
    print("You guessed the word!")
    print("You survived!")
else:
    print("You lost!")