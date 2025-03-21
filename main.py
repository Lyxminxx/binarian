from functions import binarian
from functions import unbinarian
from submenus import entoBin
from submenus import binToEn
from functions import clear
import readchar

def main_menu():
    options = ["Translate from English to Binarian", "Translate from Binarian to English", "Exit"]
    selected = 0

    while True:
        clear()
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
            if options[selected] == "Exit":
                print("Exiting...")
                clear()
                break
            elif options[selected] == "Translate from English to Binarian":
                entoBin()
            elif option[selected == "Translate from Binarian to English"]:
                binToEn()
            else:
                print(f"Selected: {options[selected]}")
                input("Press Enter to return to menu...")

if __name__ == "__main__":
    main_menu()
