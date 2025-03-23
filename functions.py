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

def is_valid_format(binary_string):
    return bool(re.fullmatch(r"\([01]{5}\)", binary_string))