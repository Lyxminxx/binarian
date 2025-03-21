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