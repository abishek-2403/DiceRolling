import random

def roll():
    a = random.randrange(1,7)
    if( a == 1):
        print(" -------")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print(" -------")
    if( a == 2):
        print(" -------")
        print("| O     |")
        print("|       |")
        print("|     O |")
        print(" -------")
    if( a == 3):
        print(" -------")
        print("| O     |")
        print("|   O   |")
        print("|     O |")
        print(" -------")
    if( a == 4):
        print(" -------")
        print("| O   O |")
        print("|       |")
        print("| O   O |")
        print(" -------")
    if( a == 5):
        print(" -------")
        print("| O   O |")
        print("|   O   |")
        print("| O   O |")
        print(" -------")
    if( a == 6):
        print(" -------")
        print("| O   O |")
        print("| O   O |")
        print("| O   O |")
        print(" -------")


print("Let's start rolling! press 'y' to continue....")
x = input()
while x.lower() == 'y':
    roll()
    print("press 'y' to roll again")
    x = input()
    if x.lower() != 'y':
        print("Thank you for playing, Come back again sometime.")