# Binarian
# Copyright (C) 2025 Sarahtonin & Lyxminx
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from wordlist import words
import random
from os import system, name
from functions import binarian, is_valid_format, clear
import re


def norToBin(level):
    wordsInLevel = words[level].copy()
    word = random.choice(wordsInLevel)
    correctTranslation = binarian(word)

    print(f'Translate {word} into binary!')
    userIn = input("Write anwser\n>")
    clear()
    if userIn == correctTranslation:
        print(f'Yes the word {word} does translate to {userIn}!')
    else:
        print(f'No, the word {word} translates to {correctTranslation}, not {userIn}. Better study some more!')
    input("Hit ENTER to continue")

def binToNor(level):
    wordsInLevel = words[level].copy()
    word = random.choice(wordsInLevel)
    correctTranslation = word
    word = binarian(word)

    print(f'Translate {word} into english!')
    userIn = input("Write anwser\n>")
    clear()
    if userIn == correctTranslation:
        print(f'Yes the word {word} does translate to {userIn}!')
    else:
        print(f'No, the word {word} translates to {correctTranslation}, not {userIn}. Better study some more!')
    input("Hit ENTER to continue")

def hangman():
    clear()
    def display_man(wrong_guesses):
        for line in hangman_art[wrong_guesses]:
            print(line)

    def display_hint(hint):
        print(" ".join(hint))
    
    def display_answer(answer):
        print(" ".join(answer))

    #Get a random word 
    word = random.choice(words[random.randint(1,5)])
    answer = binarian(word)
    answer = [chunk + ")" for chunk in answer.split(")") if chunk]
    hint = ["(xxxxx)"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True 

    hangman_art = {
        0: ("   ",
            "   ",
            "   "),
        1: (" o ",
            "   ",
            "   "),
        2: (" o ",
            " | ",     
            "   "),
        3: (" o ",
            "/| ",
            "   "),
        4: (" o ",
            "/|\\",
            "   "),
        5: (" o ",
            "/|\\",
            "/  "),
        6: (" o ",
            "/|\\",
            "/ \\")}
    
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter\n>")
        if not is_valid_format(guess):
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
        
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess 
        else:
            wrong_guesses += 1

        if hint == answer:
            display_answer(f"You win, the word was {word}! You had {wrong_guesses}.")
            input("Hit ENTER to continue")
            is_running = False
        elif hint == len(hangman_art)-1:
            display_man(wrong_guesses)
            print(f"You lose! The word was {word}! You had {wrong_guesses}.")
            input("Hit ENTER to continue")
            is_running = False
        clear()