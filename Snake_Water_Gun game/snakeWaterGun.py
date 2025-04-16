# Snake,Water,Gun Game
import random
computer = random.choice([0, -1, 1])
yourchoice = input("enter your choice: ")
youDict =   {"s": 1, "w": -1, "g": 0}
reversedict = {1:"snake", -1:"water", 0:"gun"}
you = youDict[yourchoice]
# By now we have 2 numbers (variables), you and computer
print(f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")
if (computer == you):
   print("It's draw")
else:
    if (computer == -1 and you == 1):
        print("You Win!!")
    elif (computer == -1 and you == 0):
        print("You Lose!!")
    elif (computer == 0 and you == -1):
        print( "You Win!!")
    elif (computer == 0 and you == 1):
        print( "You Lose!!")
    elif (computer == 1 and you == 0):
        print( "You Win!!")
    elif (computer == 1 and you == -1):
        print( "You Lose!!")
    else:
        print("something went wrong!!")
