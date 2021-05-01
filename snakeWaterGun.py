import random
import time
print("Welcome to SNAKE WATER GUN Game\n")
time.sleep(0.5)
a = 0
won = 0
lose = 0
tie = 0
while a < 10:
    a+=1
    i = ["SNAKE", "WATER", "GUN"]
    iRand = random.choice(i)
    #print("\n", iRand)         #hack
    ui = input("***************\nChoose: \ns for SNAKE \nw for WATER \ng for GUN\n\nPress any other key to EXIT\n\t")
    print("\n")
    time.sleep(0.5)
    if iRand == "SNAKE" and ui == "s":
        print("That is a Tie")
        tie+=1
    elif iRand == "SNAKE" and ui == "w":
        print("Computer Won")
        lose+=1
    elif iRand == "SNAKE" and ui == "g":
        print("You Won")
        won+=1
    elif iRand == "WATER" and ui == "s":
        print("You Won")
        won+=1
    elif iRand == "WATER" and ui == "w":
        print("That is a Tie")
        tie+=1
    elif iRand == "WATER" and ui == "g":
        print("Computer Won")
        lose+=1
    elif iRand == "GUN" and ui == "s":
        print("Computer Won")
        lose+=1
    elif iRand == "GUN" and ui == "w":
        print("You Won")
        won+=1
    elif iRand == "GUN" and ui == "g":
        print("That is a Tie")
        tie+=1
    else:
        exit()
    time.sleep(1)
    print(f"\nYou have won {won}, lost {lose} & tie {tie} out of {a}\n")
    time.sleep(1)
time.sleep(0.5)
print("GAME END\n")