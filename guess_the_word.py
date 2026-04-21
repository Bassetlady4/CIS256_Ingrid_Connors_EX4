# Ingrid Connors
# CIS256 Spring 2026
# Exercise Assignment 4

import random

# creating list of words that will be selected from for game
word_list = ["apple", "calendar", "bookmark", "computer", "pencil", "spatula", "bandaid", "adapter"]

word = random.choice(word_list) # selects random word from word_list
guessed_letters = [] # creates list to store wrong guesses
num_guesses = 10 # sets number of tries before game is over

# displays _ for every letter in word
display = ["_"] * len(word)

print("Get ready to play Hangman!")

while num_guesses > 0 and "_" in display:
    print("Word:", " ".join(display))
    print("Guesses left: ", num_guesses)
    guess = input("Please choose a letter: ").lower()

    if guess in guessed_letters:
        print("You have already guessed that letter. Please try again")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("That letter is not in the word. Please try again")
        num_guesses -= 1

if "_" not in display:
    print("Congratulations! You guessed the word!", word)
else:
    print("Sorry. Game over. The word was ", word)
