# File for when user wins attack

import sys
import time
from beautifultable import BeautifulTable
import mapclass as mc

# User’s lists
actions = ["explore", "quit"]
directions = ["north", "south", "east", "west"]


# When user wins
def weapon_win(message):
    """Check if user input is a positive number"""
    # While loop allows the program to contiue until
    # user puts a positive number
    while True:
        # User try to input a number
        try:
            userchoice = int(input(message))
            if userchoice > 0:
                return userchoice
            # If number is not positive user must input new number
            else:
                print("Use a positive number. Please try again.")
                continue
            # If input is not a number
        except ValueError:
            print("Invalid! Use a number. Please try again.")
            continue
            # Every time user inputs something
        finally:
            print(f"Hurry! Attack it!!")


# Using the function weapon_int to ask user to input
w = weapon_win("How many times do you want to attack? ")
print("\n")
# Print(f" You just fired {userchoice} arrows!")
print(f"{w} attack has been fired.")
time.sleep(2)  # Wait for 2 seconds
print("\n")
print("*BAM!!* *BOOM!* *HIT*")
time.sleep(2)  # Wait for 2 seconds
print("Nice Kill!")
print("\n")
time.sleep(2)  # Wait for 2 seconds
print("Where do you want to go?")
for d in directions:
    print(f"* {d}")
choice = input("Directions: ")

if choice == "north":
    Monurce = BeautifulTable()
    Monurce.rows.append(["Monurce"])
    Monurce.set_style(BeautifulTable.STYLE_BOX_DOUBLED)
    print(Monurce)
    info = mc.Mapinfo("where you can find food and treatment.")
    info.territories()
    time.sleep(3)  # Wait for 3 seconds
    print("\n")
    print("What do you want to do? ")
    for act in actions:
        print(f"* {act}")
    choice = input("Actions: ")
    if choice == "explore":
        print("You just earned 4 apples and 2 medical kit")
        print("Here's your new current inventory items...")
        time.sleep(3)  # Wait for 3 seconds
        import inventoryadditems as iai
        print(iai.newhealing_inv())
        print(iai.newconsumables_inv())
        time.sleep(3)  # Wait for 3 seconds
        print("\n")
        print("Where do you want to go? ")
        for d in directions:
            print(f"* {d}")
        choice = input("Directions: ")
        # User dies
        if choice == "north":
            MoNo = BeautifulTable()
            MoNo.rows.append(["MoNo"])
            MoNo.set_style(BeautifulTable.STYLE_BOX_DOUBLED)
            print(MoNo)
            info = mc.Mapinfo("the enemy zone. WATCH OUT! Enemies ahead!!")
            info.territories()
            time.sleep(3)  # Wait for 3 seconds
            print("\n")
            import attacking as a
            print(a.weapon_lose(""))

        # User dies
        elif choice == "south":
            MoNo = BeautifulTable()
            MoNo.rows.append(["MoNo"])
            MoNo.set_style(BeautifulTable.STYLE_BOX_DOUBLED)
            print(MoNo)
            info = mc.Mapinfo("the enemy zone. WATCH OUT! Enemies ahead!!")
            info.territories()
            time.sleep(3)  # Wait for 3 seconds
            print("\n")
            import attacking as a
            print(a.weapon_lose(""))

        # User dies
        elif choice == "east":
            MoNo = BeautifulTable()
            MoNo.rows.append(["MoNo"])
            MoNo.set_style(BeautifulTable.STYLE_BOX_DOUBLED)
            print(MoNo)
            info = mc.Mapinfo("the enemy zone. WATCH OUT! Enemies ahead!!")
            info.territories()
            time.sleep(3)  # Wait for 3 seconds
            print("\n")
            import attacking as a
            print(a.weapon_lose(""))

        # Amulet is found
        elif choice == "west":
            Mountik = BeautifulTable()
            Mountik.rows.append(["Mountik"])
            Mountik.set_style(BeautifulTable.STYLE_BOX_DOUBLED)
            print(Mountik)
            info = mc.Mapinfo("where the amulet is! You found it!")
            info.territories()
            print("\n")
            time.sleep(2)  # Wait for 2 seconds
            print("Lets go to MonuLiberty!")
            print("\n")
            time.sleep(2)  # Wait for 2 seconds
            MonuLiberty = BeautifulTable()
            MonuLiberty.rows.append(["MonuLiberty"])
            MonuLiberty.set_style(BeautifulTable.STYLE_BOX_DOUBLED)
            print(MonuLiberty)
            info = mc.Mapinfo("the ending base. Victory! You completed the quest and destroyed Zuko!")
            info.territories()
            print("Congratulation. See you next time!")
            sys.exit()

        else:
            print("Invalid choice.")
            sys.exit()

    elif choice == "quit":
        print("Bye Bye!")
        sys.exit()

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

else:
    print("Invalid choice!")
    sys.exit()

