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
    A player has exactly 8 tries and enters letters. Nothing changes if a player has more tries left but they have already guessed the word.
    If the letter doesn't appear in the word, the computer takes one try away – even if the user has already guessed this letter.
    If the player doesn't have any more attempts, the game should end and the program should show a losing message. Otherwise, the player can continue to input letters.
    Also, the word should be selected from our list: 'python', 'java', 'kotlin', 'javascript', so that your program can be tested more reliably.
'''

print("H A N G M A N")
print("\n\n")
hidden_words = ['python', 'java', 'kotlin', 'javascript']
hidden_word = hidden_words[random.randint(0, len(hidden_words) - 1)]  # picks a random word
word_display = ("-" * (len(hidden_word)))  # formats the word to provide a hint
remaining_attempts = 8
guessed_letters = []
while remaining_attempts > 0:  # Looping structure until user is out of attempts
    print(f"{word_display}")  # display the word, hidden by "-"
    guess = input("Input a letter: ")  # Prompts user for a guess(with hint provided) and stores as a string
    guessed_letters.append(guess)  # adds guess to list of guessed_letters
    if guess not in hidden_word:  # checks if the users guess is a part of the hidden_word and outputs message if it is not
        print("That letter doesn't appear in the word")
    temp_display = hidden_word  # copy of hidden_word
    for letters in hidden_word:  # parses through every character in hidden_word
         if letters not in guessed_letters:  # boolean check if a character in hidden_word is a part of guessed_letters
             temp_display = temp_display.replace(letters, "-")  #replaces every character that fulfils the above requirements with "-"
    word_display = temp_display  # overwrite what is display at the start of the loop
    remaining_attempts -= 1  # lowers remaining attempts
    print("\n")  # new line for formatting

print("Thanks for playing!")
print("We'll see how well you did in the next stage")