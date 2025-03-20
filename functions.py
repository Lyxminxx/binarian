from alphabet import alphabet
from os import system, name


def binarian(word):
    wordBin = ""  
    word = word.lower()
    for letter in word:
        if letter in alphabet.keys():  
            wordBin += alphabet[letter]
        elif letter == " ":
            wordBin += " "
        else:
            wordBin += letter
    return wordBin

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')