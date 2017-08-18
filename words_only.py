#!/usr/local/bin/python3
'''
This is a simple hangman-style word game. The user runs this script, a random
word is selected, and then they have n-1 chances to guess the word, where
n is the number of characters in the word. This program assumesinput
of only one character at a time.

:author: Chris Byrd <christopher.byrd2013@gmail.com>
:date: 2017-08-18
'''

import random  # used to select random element from list


def get_hint(word, already_guessed):
    # take the selected word and a list of letters already guessed.
    # generate a string with all correctly guessed letters and underscores
    hint_string = ''
    for letter in word:
        if letter in correctly_guessed:
            hint_string += '{} '.format(letter.upper())
        else:
            hint_string += '_ '
    return hint_string


with open('files/words.txt', 'r') as file:
    # read all text from file. Split data on newlines into a list
    data = file.read()
    words = data.splitlines()
    file.close()

random_word = random.choice(words)  # get random word from the list

# initialize list to keep track of guessed words
already_guessed = []
correctly_guessed = []

# get the number of letters in the word, then subtract 1
num_chances = len(random_word) - 1

while True:
    hint_string = get_hint(random_word, already_guessed)

    if '_' not in hint_string or num_chances == 0:
        # no underscore in hint_string so we've guessed all correct letters
        break

    print(hint_string)
    answer = input('Guess a letter: ')

    answer.lower()  # convert to lowercase

    if answer in random_word:
        if answer not in correctly_guessed:
            correctly_guessed.append(answer)  # add to the list
        else:
            # the letter is in the word, but they've already guessed it
            print('You\'ve already guessed that letter. Try again!')
    else:
        print('Sorry, guess another letter.')
        num_chances -= 1  # decrement the number of chances by 1
    already_guessed.append(answer)  # add to the list

if num_chances > 0:
    # There are still chances left - we can deduce they've guessed all letters
    print('Congrats!', end='')  # end='' tells print to not add a newline
else:
    # If there aren't chances left then they have not guessed the word
    print('Sorry!', end='')  # end='' tells print to not add a newline

print(' The word was {}'.format(random_word))
