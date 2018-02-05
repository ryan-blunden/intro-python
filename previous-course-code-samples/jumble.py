#!/usr/bin/env python3
import random

wordlist = ['alphabet', 'monstrosity', 'fastidious']
word = random.choice(wordlist)
list_of_letters = list(word)
random.shuffle(list_of_letters)
scrambled_word = ''.join(list_of_letters)

for num_guesses in range(1, 6):
    guess = input(scrambled_word + '? ')
    if guess == word:
        print('You got it!')
        break
else:
    print("You're not very good at this, are you?")
