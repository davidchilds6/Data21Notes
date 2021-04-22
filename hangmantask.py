# # Code a hangman game, start simple and then add more complex features
# # use the list from hangman_words.py as arguments in your functions

import random
# Select word from the hangman_words word_list
from hangman_words import word_list, hangman_pics


def select_word(list):
    word = random.randint(0, len(list) - 1)
    return list[word]


# print(select_word(word_list))
# Make a function that ensures that the user inputs to the game correctly.


def display_the_board(missed_letters, correct_letters, hidden_word):
    print(hangman_pics[len(missed_letters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(hidden_word)

    for i in range(len(hidden_word)):  # Replace blanks with correctly guessed letters
        if hidden_word[i] in correct_letters:
            blanks = blanks[:i] + hidden_word[i] + blanks[i + 1:]

    for letter in blanks:  # Show the secret word with spaces in between each letter.
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


missed_letters = ""
correct_letters = ""
word = select_word(word_list)
game_done = False
while True:
    display_the_board(missed_letters, correct_letters, word)

    guess = player_guess(missed_letters + correct_letters)

    if guess in word:
        correct_letters = correct_letters + guess

        found_all_letters = True
        for i in range(len(word)):
            if word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print(f"Well done the word was {word}")
            game_done = True
    else:
        missed_letters = missed_letters + guess

        if len(missed_letters) == len(hangman_pics) - 1:
            display_the_board(missed_letters, correct_letters, word)
            print(f"Game over, the word was {word}")
            game_done = True

    if game_done:
        break
