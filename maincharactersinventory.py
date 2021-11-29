# File for main character's inventory

import time
from beautifultable import BeautifulTable

# List of available main charcaters
characters = ["kuro", "adachi"]

# Table for kuro's inventory if user picks kuro
kuro = BeautifulTable()
kuro.rows.append([1])
kuro.rows.append([5000])
kuro.rows.append([0])
kuro.rows.append([0])
kuro.rows.append(["sword"])
kuro.rows.header = ["Level:", "MAX HP:", "Damage:", "Kills:", "Default Weapon:"]
kuro.set_style(BeautifulTable.STYLE_BOX)

# Table for adachi's inventory if user picks adachi
adachi = BeautifulTable()
adachi.rows.append([1])
adachi.rows.append([5000])
adachi.rows.append([0])
adachi.rows.append([0])
adachi.rows.append(["sword"])
adachi.rows.header = ["Level:", "MAX HP:", "Damage:", "Kills:", "Default Weapon:"]
adachi.set_style(BeautifulTable.STYLE_BOX)


def char_inv1():
    """" Output Kuro's inventory"""
    print("Kuro's Inventory:")
    print(kuro)


def char_inv2():
    """" Output Adachi's inventory"""
    print("Adachi's Inventory:")
    print(adachi)


print("Choose a character:")
for c in characters:
    print(f"* {c}")


def characterchoices(message):
    """Test for checking if an input is a valid character """
    # The while loop makes sure the program continues until the user
    # has inputted a valid character
    while True:
        # The try statement attempts to exceute the user input
        try:
            userInput = str(input(message))
            # The if-else statement tests to see if the character is valid
            # If the character is valid then the program continues
            if userInput == "kuro":
                print("\n")
                char_inv1()
                import maincharactersclass as mcc
                info = mcc.Info("Kuro")
                info.intro_kuro()
                return userInput
            elif userInput == "adachi":
                print("\n")
                char_inv2()
                import maincharactersclass as mcc
                info = mcc.Info("Adachi")
                info.intro_adachi()
                return userInput
            # If the character is invalid then the user must
            # try again
            else:
                print("Invalid choice. Please try again.")
                continue
        # If the user did not input a character, the user is prompted to try again
        except NameError:
            print("Input is not available. Try again.")
            continue

# Using the function characterchoices to ask for the user inputs
choice = characterchoices("Character: ")
print(choice)

time.sleep(4)  # Wait for 4 seconds
print("\n")
print("Now, let's have a look on your current inventory items...")
import inventoryitems as ii
print(ii.healing_inv())
print(ii.consumables_inv())
time.sleep(4)  # Wait for 4 seconds

print("\n")
print("Lets begin our mission.")
time.sleep(2)  # Wait for 2 seconds
print("QUEST: Start at MonuBorder and go to Mountik to find the amulet. Good Luck!")
time.sleep(4)  # Wait for 4 seconds
print("\n")
print("Here's the map of Monu Village...")
time.sleep(4)  # Wait for 4 seconds
import mapa
print(mapa.monu_ter())
time.sleep(3)  # Wait for 3 seconds
print("Let's Start!")
print("\n")

time.sleep(2)  # Wait for 2 seconds
MonuBorder = BeautifulTable()
MonuBorder.rows.append(["MonuBorder"])
MonuBorder.set_style(BeautifulTable.STYLE_BOX_DOUBLED)
print(MonuBorder)

import mapclass as mc
info = mc.Mapinfo("the starting base.")
info.territories()

print("\n")
time.sleep(2)  # Wait for 2 seconds
import directions as d
print(d.directionchoices(""))

