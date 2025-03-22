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

from functions import *

def translateEnToBin():
    userIn = input("Enter english word/sentence\n>")
    print(binarian(userIn))
    input("Hit ENTER to continue")

def translateBinToEn():
    userIn = input("Enter binarian word/sentence\n>")
    print(unbinarian(userIn))
    input("Hit ENTER to continue")