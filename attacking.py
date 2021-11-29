# File for when user loses attack

import sys
import time

# When user dies
def weapon_lose(message):
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
l = weapon_lose("How many times do you want to attack? ")
print("\n")
# Print(f" You just fired {userchoice} arrows!")
print(f"{l} attack has been fired.")
time.sleep(2)  # Wait for 2 seconds
print("\n")
print("*BAM!!* *BOOM!* *HIT*")
time.sleep(3)  # Wait for 3 seconds
print("GAME OVER. There was too many of them. You died. Better luck next time.")
sys.exit()

