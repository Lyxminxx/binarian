from functions import *

def translateEnToBin():
    userIn = input("Enter english word/sentence\n>")
    print(binarian(userIn))
    input("Hit ENTER to continue")

def translateBinToEn():
    userIn = input("Enter binarian word/sentence\n>")
    print(unbinarian(userIn))
    input("Hit ENTER to continue")