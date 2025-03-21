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

import re

def unbinarian(encoded_text):
    from alphabet import alphabet
    
    reverse_alphabet = {v: k for k, v in alphabet.items()}
    
    decoded = re.sub(r"\(\d{5}\)", lambda m: reverse_alphabet.get(m.group(), m.group()), encoded_text)
    
    return decoded


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')