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

from submenus import entoBin, binToEn, translateMenu
from functions import clear
import readchar

def main_menu():
    options = ["Translate from English to Binarian","Translate from Binarian to English","Translate","Exit"]
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
            elif options[selected] == "Translate from Binarian to English":
                binToEn()
            elif options[selected] == "Translate":
                translateMenu()

if __name__ == "__main__":
    main_menu()
