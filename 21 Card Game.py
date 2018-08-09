import random
import math 

def start_game ():
    """Function start_game initiates game-play and decides if the user or the computer will take the first turn"""
    print("New Game start")
    choice = input("Do you want to go first (y/n): ")
    
    if choice == "y":
        user()
    if choice == "n":
        cpu_always_wins()

def user():
    """Function user is the cycle of the game-play if the user decides to accept the offer of taking the first turn of the game"""
    cards = 21
    while cards != 0:
        print("-----------------------------------------")
        print("")
        print("There are " + str(cards) + " cards left")
        print("")

        userPick = -1 #initializes a value that cannot be entered by the user
        while check(userPick, cards) == False:
            userPick = int(input("How many cards do you pick (1-3): "))
            print("      You picked " + str(userPick) + " cards")
            if check(userPick, cards) == False:
                print("       Cannot pick " + str(userPick) + " cards")

        cards = cards - userPick
        if cards == 0:
            print("")
            print("You WIN! Game over.")
            break
        for x in range(2):
            print("")
        print("There are " + str(cards) + " cards left")
        print("")
        computer_pick = computer_choice(cards)

        if computer_pick == 1:
            print("      I pick " + str(computer_pick) + " card")
            print("")
        else:
            print("      I pick " + str(computer_pick) + " cards")
            print("")
        if cards == 0:
            print("I WIN! Game over.")
            
        cards = cards - computer_pick #updates the card count

def computer_choice(cards):
    """Function computer_choice chooses a random integer between 1 & 3"""
    if cards >= 3:
        choice = random.randint(1,3)
        return choice
    if cards == 2:
        choice = random.randint(1,2) #range narrowed down to between 1-2
        return choice
    else:
        choice = 1
        return choice

def guaranteed_win(cards):
    """This function strategically guarantees the computer to win if it makes the first move by choosing the number of cards based upon the remainder of the amount of cards left in regards to divisibility to four"""
    if cards == 21:
        return 1
    else:
        choice = (cards % 4)
        return choice

def cpu_always_wins():
    """This function allows for the computer to always win if the user declines taking the first turn"""
    cards = 21
    while cards != 0:
        print("-------------------------------------------")
        print("")
        print("There are " + str(cards) + " cards left")
        print("")
        computer_pick = guaranteed_win(cards)
        
        if computer_pick == 1:
            print("      I pick " + str(computer_pick) + " card")

        else:
            print("      I pick " + str(computer_pick) + " cards")
    
        cards = cards - computer_pick
        if cards == 0:
            print("")
            print("I WIN! Game over.")
            break

        for x in range(2):
            print("")
        print("There are " + str(cards) + " cards left")
        print("")
                 
        userPick = -1
        while check(userPick, cards) == False:
            userPick = int(input("How many cards do you pick (1-3): "))
            if check(userPick, cards) == False:
                print("      Cannot pick " + str(userPick) + " cards")

        cards = cards - userPick
        if cards == 0:
                print("You WIN! Game over.")
        print("      You picked " + str(userPick) + " cards")
        print("")

def check(userPick, cards):
    """Function check evalutes the input and determines if it is a valid number (within the range 1-3). If it is valid it returns True and if False, it prompts the user to re-enter a valid number"""
    total = cards - userPick
    if total == 0: #when there are no cards left to draw
        return " You WIN! Game over."
    if userPick < 1 or userPick > 3 or cards - userPick < 0: #sets parameters for invalid input
        return False
    elif userPick >= 1 and userPick <=3 and userPick <= cards: #valid inputs
        return True
    else:
        return True

start_game()


        
    
    
