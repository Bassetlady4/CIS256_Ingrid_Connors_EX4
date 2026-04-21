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
