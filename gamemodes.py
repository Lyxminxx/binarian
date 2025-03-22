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
from functions import binarian
from functions import clear

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