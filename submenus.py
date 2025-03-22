import readchar
from gamemodes import norToBin, binToNor
from functions import clear
from translate import translateEnToBin, translateBinToEn  # Ensure these are correctly imported

def entoBin():
    options = ["Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Back to main menu"]
    selected = 0

    while True:
        clear()
        print("Select a level to start translating!")
        print("Use arrow keys to navigate and Enter to select:\n")

        for i, option in enumerate(options):
            prefix = "> " if i == selected else "  "
            print(f"{prefix}{option}")

        key = readchar.readkey()

        if key == readchar.key.UP and selected > 0:
            selected -= 1
        elif key == readchar.key.DOWN and selected < len(options) - 1:
            selected += 1
        elif key == readchar.key.ENTER:
            if selected < 5:  # If it's a level
                clear()
                norToBin(selected + 1)
            else:  # Back to main menu
                print("Exiting...")
                break

def binToEn():
    options = ["Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Back to main menu"]
    selected = 0

    while True:
        clear()
        print("Select a level to start translating!")
        print("Use arrow keys to navigate and Enter to select:\n")

        for i, option in enumerate(options):
            prefix = "> " if i == selected else "  "
            print(f"{prefix}{option}")

        key = readchar.readkey()

        if key == readchar.key.UP and selected > 0:
            selected -= 1
        elif key == readchar.key.DOWN and selected < len(options) - 1:
            selected += 1
        elif key == readchar.key.ENTER:
            if selected < 5:
                clear()
                binToNor(selected + 1)
            else:
                print("Exiting...")
                break

def translateMenu():
    options = ["Binarian to English", "English to Binarian", "Back to main menu"]
    selected = 0

    while True:
        clear()
        print("Select if you want to translate from or to Binarian!")
        print("Use arrow keys to navigate and Enter to select:\n")

        for i, option in enumerate(options):
            prefix = "> " if i == selected else "  "
            print(f"{prefix}{option}")

        key = readchar.readkey()

        if key == readchar.key.UP and selected > 0:
            selected -= 1
        elif key == readchar.key.DOWN and selected < len(options) - 1:
            selected += 1
        elif key == readchar.key.ENTER:
            if selected == 0:
                clear()
                translateBinToEn()
            elif selected == 1:
                clear()
                translateEnToBin()
            else:
                print("Exiting...")
                break
