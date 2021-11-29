# Coarse: CS 30
# Period:3
# Date created: 27/10/21
# Date last modified: 17/11/28
# Name: Rabi Jasteen Juancito
# Description: RPG Classes - main game

import sys
import time
from beautifultable import BeautifulTable

# Title of the game
start = BeautifulTable()
start.rows.append(["THE MONU VILLAGE"])
start.set_style(BeautifulTable.STYLE_BOX_DOUBLED)
print(start)
print("\n")
# User inputs enter if they want to play
user = input("Press 'Enter' to play \n")

if user == "":
    print("Hey Traveler!")
    time.sleep(2)  # Wait for 2 seconds
    print("Welcome to Monu Village! This is a one path adaventure game.")
    time.sleep(2)  # Wait for 2 seconds
    print("Which means there's only one path to you can win this game.")
    time.sleep(2)  # Wait for 2 seconds
    print("Wish you luck!")

    print("\n")
    time.sleep(3)  # Wait for 3 seconds
    # Ask user to inuput a username they want
    name = (input("What is your character username: "))
    print(f"Cool username {name}!")
    print("\n")

    time.sleep(2)  # Wait for 2 seconds
    print(f"Alright {name}, let me tell you about the history of the Monu Village...")
    time.sleep(3)  # Wait for 3 seconds
    print("Half of your ancestors died after an explosion that occurred when Zuko, the greatest enemy invaded the Monu Village.")
    time.sleep(3)  # Wait for 3 seconds
    print("You now want to take revenge for your ancestors losts and destroy Zuko.")
    time.sleep(3)  # Wait for 3 seconds
    print("In order to destroy him you must find the amulet your ancentors left for you in the Mountik.")
    time.sleep(3)  # Wait for 3 seconds

    print("\n")
    import maincharactersinventory as mci
    print(mci.characterchoices(""))

else:
    print("Come back next time!")
    sys.exit()

