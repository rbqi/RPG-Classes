# File for character's message for user

# Parent Class
class Character:
    """Class for partners given name, power and info"""

    def __init__(self, name):
        self.name = name

    def intro_kuro(self):
        print("From Kuro: \n", "Hey! I'm", self.name + "!", "It's nice to meet you. Glad you picked me.")

    def intro_adachi(self):
        print("From Adachi: \n", "Hey Partner! I'm", self.name + "!", "It's nice to meet you. Glad you picked me.")


# Child class
class Info(Character):
    """Represent info of the partner's background"""

Kuro = Info("Kuro")
Adachi = Info("Adachi")

