# File for directions and actions

import time
from beautifultable import BeautifulTable
import mapclass as mc


# User’s lists
actions = ["explore", "quit"]
directions = ["north", "south", "east", "west"]


# Fuction for direction inputs
def directionchoices(message):
    """Ask user where they want to go"""
    print("Where do you want to go? ")
    for d in directions:
        print(f"* {d}")
    """Test for checking if an input is a valid direction """
    # The while loop makes sure the program continues until the user
    # has inputted a valid direction
    while True:
        # The try statement attempts to exceute the user input
        try:
            userInput = str(input(message))
            # The if-else statement tests to see if the direction is valid
            # If the direction is valid then the program continues
            # User dies
            if userInput == "north":
                MV = BeautifulTable()
                MV.rows.append(["MoNo"])
                MV.set_style(BeautifulTable.STYLE_BOX_DOUBLED)
                print(MV)
                info = mc.Mapinfo("the enemy zone. WATCH OUT! Enemies ahead!!")
                info.territories()
                time.sleep(3)  # Wait for 3 seconds
                import attacking as a
                print(a.weapon_lose(""))
                return userInput

            # User dies
            elif userInput == "south":
                MV = BeautifulTable()
                MV.rows.append(["MoNo"])
                MV.set_style(BeautifulTable.STYLE_BOX_DOUBLED)
                print(MV)
                info = mc.Mapinfo("the enemy zone. WATCH OUT! Enemies ahead!!")
                info.territories()
                time.sleep(3)  # Wait for 3 seconds
                import attacking as a
                print(a.weapon_lose(""))
                return userInput

            # User dies
            elif userInput == "east":
                MoNo = BeautifulTable()
                MoNo.rows.append(["MoNo"])
                MoNo.set_style(BeautifulTable.STYLE_BOX_DOUBLED)
                print(MoNo)
                info = mc.Mapinfo("the enemy zone. WATCH OUT! Enemies ahead!!")
                info.territories()
                time.sleep(3)  # Wait for 3 seconds
                import attacking as a
                print(a.weapon_lose(""))
                return userInput

            # User wins
            elif userInput == "west":
                MV = BeautifulTable()
                MV.rows.append(["MV"])
                MV.set_style(BeautifulTable.STYLE_BOX_DOUBLED)
                print(MV)
                info = mc.Mapinfo("empty.")
                info.territories()
                time.sleep(2)  # Wait for 2 seconds
                print("Where do you want to go?")
                for d in directions:
                    print(f"* {d}")
                choice = input("Directions: ")

                # User wins
                if choice == "north":
                    MoNo = BeautifulTable()
                    MoNo.rows.append(["MoNo"])
                    MoNo.set_style(BeautifulTable.STYLE_BOX_DOUBLED)
                    print(MoNo)
                    info = mc.Mapinfo("the enemy zone. WATCH OUT! Enemies ahead!!")
                    info.territories()
                    time.sleep(3)  # Wait for 3 seconds
                    import attackwin as aw
                    print(aw.weapon_win(""))
                    return choice
                # User dies
                elif choice == "south":
                    MoNo = BeautifulTable()
                    MoNo.rows.append(["MoNo"])
                    MoNo.set_style(BeautifulTable.STYLE_BOX_DOUBLED)
                    print(MoNo)
                    info = mc.Mapinfo("the enemy zone. WATCH OUT! Enemies ahead!!")
                    info.territories()
                    time.sleep(3)  # Wait for 3 seconds
                    import attacking as a
                    print(a.weapon_lose(""))
                    return choice
                # User dies
                elif choice == "east":
                    MoNo = BeautifulTable()
                    MoNo.rows.append(["MoNo"])
                    MoNo.set_style(BeautifulTable.STYLE_BOX_DOUBLED)
                    print(MoNo)
                    info = mc.Mapinfo("the enemy zone. WATCH OUT! Enemies ahead!!")
                    info.territories()
                    time.sleep(3)  # Wait for 3 seconds
                    import attacking as a
                    print(a.weapon_lose(""))
                    return choice
                # User dies
                elif choice == "west":
                    MoNo = BeautifulTable()
                    MoNo.rows.append(["MoNo"])
                    MoNo.set_style(BeautifulTable.STYLE_BOX_DOUBLED)
                    print(MoNo)
                    info = mc.Mapinfo("the enemy zone. WATCH OUT! Enemies ahead!!")
                    info.territories()
                    time.sleep(3)  # Wait for 3 seconds
                    import attacking as a
                    print(a.weapon_lose(""))
                    return choice

                else:
                    print("Invalid choice. Please try again.")
                    continue
            else:
                print("Invalid choice. Please try again.")
                continue
        # If the user did not input a character, the user is prompted to try again
        except NameError:
            print("Input is not available. Try again.")
            continue
# Using the function characterchoices to ask for the user inputs
choice = directionchoices("Direction: ")
print(choice)

