# # Code a hangman game, start simple and then add more complex features
# # use the list from hangman_words.py as arguments in your functions

import random
# Select word from the hangman_words word_list
from hangman_words import word_list, hangman_pics


def select_word(list):  # This function takes a random word from a list for the player to guess
    word = random.randint(0, len(list) - 1)
    return list[word]


def display_the_board(wrong_guesses, correct_guesses, hidden_word):  # This function draws the board for each go
    print(hangman_pics[len(wrong_guesses)])  # with no wrong guesses, will print index 0 of 'hangman_pics'
    print()

    print('Wrong letters:', end=' ')  # Incorrect guesses will go here
    for letter in wrong_guesses:
        print(letter, end=' ')  # Incorrect guesses printed on same line with one space in between
    print()

    blanks = '_' * len(hidden_word)  # Initialise a variable with only underscores.

    for letter in range(len(hidden_word)):  # Replace blanks with correctly guessed letters
        if hidden_word[letter] in correct_guesses:  # slots in the correct guess between underscores.
            blanks = blanks[:letter] + hidden_word[letter] + blanks[letter + 1:]

    for letter in blanks:  # Show the hidden word with spaces in between each letter.
        print(letter, end=' ')
    print()


# This function asks for your guess and makes sure that your guess is valid and lowercase.
def player_guess(guessed_list):
    while True:
        print("What is your guess?")
        guess = input().lower()
        if len(guess) != 1:
            print("Your guess must be one letter.")
        elif guess in guessed_list:
            print("You've already tried that letter.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Your guess has to be a letter.")
        else:
            return guess


wrong_letters = ""  # Initialise empty strings for wrong guesses and correct guesses
correct_letters = ""
word = select_word(word_list)  # Word is selected from the list
game_done = False  # This boolean will help us to stop the game when won or lost.
while True:
    display_the_board(wrong_letters, correct_letters, word)  # Call the display the board function.

    guess = player_guess(wrong_letters + correct_letters)  # Make sure the guess satisfies the input criteria before moving on.

    if guess in word:
        correct_letters = correct_letters + guess  # Populates correct_letters if in the word

        found_all_letters = True
        for i in range(len(word)):  # This for loop checks each index in the word
            if word[i] not in correct_letters:
                found_all_letters = False  # if the index isn't in the correct letters we haven't finished yet
                break
        if found_all_letters:  # Is True
            print(f"Well done the word was {word}")
            game_done = True  # breaks the while loop and ends the game if won.
    else:
        wrong_letters = wrong_letters + guess

        if len(wrong_letters) == len(hangman_pics) - 1:  # If the number of incorrect guess = len of pic list, no more goes.
            display_the_board(wrong_letters, correct_letters, word)
            print(f"Game over, the word was {word}")
            game_done = True # breaks the while loop and ends the game when lost.

    if game_done:
        break
