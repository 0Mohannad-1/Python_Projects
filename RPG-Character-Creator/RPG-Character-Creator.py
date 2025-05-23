class Character:
    def __init__(self, CharacterName, ClassName=True):
        self.CharacterName = CharacterName
        self.ClassName = ClassName
        self.hp = 100
        self.mana = 100
        self.strength = 10
    
    def Show_Stats(self):
        print(f"Hello, {self.CharacterName} And Welcome To The Game!")
        print(" ")
        print("Your Attributes As A Warrior: ")
        print("+---------------------+")
        print(f"| Your Hp: {self.hp + 50}        |")
        print(f"| Your mana: {self.mana}      |")
        print(f"| Your strength: {self.strength}   |")
        print("+---------------------+")
        print(" ")
        print("Your Attributes As A Mage: ")
        print("+---------------------+")
        print(f"| Your Hp: {self.hp}        |")
        print(f"| Your mana: {self.mana + 50}      |")
        print(f"| Your strength: {self.strength}   |")
        print("+---------------------+")

class Warrior(Character):
     def Show_Warrior_Stats(self): 

        print("+---------------------+")
        print(f"| Your Hp: {self.hp + 50}        |")
        print(f"| Your mana: {self.mana}      |")
        print(f"| Your strength: {self.strength}   |")
        print("+---------------------+")

class Mage(Character):
     def Show_Mage_Stats(self):

        print("+---------------------+")
        print(f"| Your Hp: {self.hp}        |")
        print(f"| Your mana: {self.mana + 50}      |")
        print(f"| Your strength: {self.strength}   |")
        print("+---------------------+")
            

CharacterName = ' '.join(input("Please Enter The Username Of Your Character: ").strip().title().split())
print(" ")

Game = Character(CharacterName)

Game.Show_Stats()

print(" ")

while True:
    ClassName = input("Pick A Class To Play With, Warrior Or Mage: ").capitalize()
    print(" ")
    Warrior_Class = Warrior(CharacterName, ClassName)
    Mage_Class = Mage(CharacterName, ClassName)

    if ClassName == "Warrior":
            print("You Have Picked A Warrior As Your Class!")
            print("Here Are Your Attributes As A Warrior")
            Warrior_Class.Show_Warrior_Stats()
            break

    elif ClassName == "Mage":
            print("You Have Picked A Mage As Your Class!")
            print("Here Are Your Attributes As A Mage")
            Mage_Class.Show_Mage_Stats()
            break

    else:
            print("Wrong Class Please Try Again")