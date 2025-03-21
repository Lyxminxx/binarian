import readchar
from gamemodes import norToBin
from gamemodes import binToNor
from functions import clear
def entoBin():
        options = ["Level 1", "Level 2", "Level 3","Level 4", "Level 5" , "Back to main menu"]
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
                if options[selected] == "Level 1":
                    clear()
                    norToBin(1)
                elif options[selected] == "Level 2":
                    clear()
                    norToBin(2)
                elif options[selected] == "Level 3":
                    clear()
                    norToBin(3)
                elif options[selected] == "Level 4":
                    clear()
                    norToBin(4)
                elif options[selected] == "Level 5":
                    clear()
                    norToBin(5)
                elif options[selected] == "Back to main menu":
                    print("Exiting...")
                    break
                else:
                    print(f"Selected: {options[selected]}")

def binToEn():
        options = ["Level 1", "Level 2", "Level 3","Level 4", "Level 5" , "Back to main menu"]
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
                if options[selected] == "Level 1":
                    clear()
                    binToNor(1)
                elif options[selected] == "Level 2":
                    clear()
                    binToNor(2)
                elif options[selected] == "Level 3":
                    clear()
                    binToNor(3)
                elif options[selected] == "Level 4":
                    clear()
                    binToNor(4)
                elif options[selected] == "Level 5":
                    clear()
                    binToNor(5)
                elif options[selected] == "Back to main menu":
                    print("Exiting...")
                    break
                else:
                    print(f"Selected: {options[selected]}")
