from wordlist import words
import random
from os import system, name
from functions import binarian
from functions import clear

def norToBin(level):
    wordsInLevel = []
    for word, word_level in words.items():
        if word_level == level:
            wordsInLevel.append(word)
    word = random.choice(wordsInLevel)
    correctTranslation = binarian(word)

    print(f'Translate {word} into binary!')
    userIn = input("Write anwser\n>")
    clear()
    if userIn == correctTranslation:
        print(f'Yes the word {word} does translate to {userIn}!')
    else:
        print(f'No, the word {word} translates to {correctTranslation}. Better study some more!')

norToBin(2)