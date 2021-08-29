'''
Filename: nim.py
It is the misere version of a game called nim. In this version, you want the opponent to remove the last number!
'''

import sys
import random


def inputManager(pile): #this fucntions mananges the input from the user!

    if pile >= 3:
        req = "\nWhat numbers do you want to remove(1, 2, or 3)? Press 'q' to quit. "
    elif pile >= 2 and pile < 3:
        req = "\nWhat numbers do you want to remove(1 or 2)? Press 'q' to quit. " 

    playp = input(req)

    while playp != "1" or playp != "2" or playp != "3" or playp != "q":
        try:
            if playp == "1" or playp == "2" or playp == "3" or playp == "q":
                return playp
        except ValueError:
            print("Try again!")

        playp = input(req)


    '''
    This functions returns True if the player wins and False if the computer wins.
    It also prints results after every move. 
    There are special rules when pile is 3 or lesser for computer's turn.
    '''
def game(pile): 

    greater4 = True
    while greater4 == True: #As long as the pile size remains greater than 4, this loop will run.

        playp = inputManager(pile)

        if playp == "q":
            return None

        if pile == 4 and playp == "3":
            playp = int(playp)
            newpile = pile - playp
            print("\nPlayer removed: ", playp)
            print("Remaining pile: ", newpile)
            print("Computer lost")
            return True
        
        else:
            playp = int(playp)
            newpile = pile - playp
            print("\nPlayer removed: ", playp)
            print("Remaining pile: ", newpile)

            comp = random.randint(1, 3)
            
            if newpile == 4 and comp == 3:
                nnewpile = newpile - comp
                print("Computer removed: ", comp)
                print("Remaining pile: ", nnewpile)
                print("Player lost")
                return False

            elif newpile == 3:
                comp = 2
                nnewpile = newpile - comp
                print("Computer removed: ", comp)
                print("Remaining Pile: ", nnewpile)
                print("Player lost")
                return False

            elif newpile == 2:
                comp = 1
                nnewpile = newpile - comp
                print("Computer removed:", comp)
                print("Remaining pile: ", nnewpile)
                print("Player lost")
                return False

            else:
                nnewpile = newpile - comp
                print("Computer removed: ", comp)
                print("Remaining pile: ", nnewpile)
                pile = nnewpile

                if nnewpile < 4:
                    greater4 = False
        
    if pile == 2:
            
            playp = inputManager(pile)

            if playp == "q":
                return None
 
            if playp == "2":
                playp = int(playp)
                newpile = pile - playp
                print("\nPlayer removed: ", playp)
                print("Remaining pile: ", newpile)
                print("Player lost")
                return False
            
            elif playp == "1":   
                playp = int(playp)
                newpile = pile - playp
                print("\nPlayer removed: ", playp)
                print("Remaining pile: ", newpile)
                print("Computer lost")
                return True
        
    elif pile == 3:
            
                playp = inputManager(pile)

                if playp == "q":
                    return None

                if playp == "3":
                    playp = int(playp)
                    newpile = pile - playp
                    print("\nPlayer removed:", playp)
                    print("Remaining pile: ", newpile)
                    print("Player lost")
                    return False
                
                elif playp == "2":
                    playp = int(playp)
                    newpile = pile - playp
                    print("\nPlayer removed: ", playp)
                    print("Remaining pile: ", newpile)
                    print("Computer Lost")
                    return True
                
                elif playp == "1":   
                    playp = int(playp)
                    newpile = pile - playp
                    print("\nPlayer removed: ", playp)
                    print("Remaining pile: ", newpile)
                    comp = 1
                    nnewpile = newpile - comp
                    print("Computer removed: ", comp)
                    print("Remaining pile: ", nnewpile)
                    print("Player lost")
                    return True



def pileGen(): #This function generates and returns pile of random size from 9 to 21.

    pile = random.randint(9, 21)
    print("\nThe pile: ", pile)
    return pile



def playAgain(): #This function asks the user if they want to play again or not.

    again = input("\nDo you want to play again? Press 'y' for yes or 'n' for no! ")

    while again != "y" or again != "n":
        try:
            if again == "y":
                return True
            elif again == "n":
                return False

        except ValueError:
            print("Come on!")
        again = input("\nCome on!! Do you want to play again? Press 'y' for yes or 'n' for no! ")
    

def main(): #The main keeps count of total score after every game and print it. It exits the game if the user does not want to play.

    print ("\nWelcome, this game is a version of the game nim. In this version, you can cut out the pile by 1, 2, or 3. The goal of this game is to make the opponent end the pile. ")
    print ("For example, if the pile is 4, you could cut out 3, and thus the opponent would lose! \n\nLet's start!!")
    
    playerwins = 0
    computerwins = 0
    aplay = True
    while aplay == True:

        pile = pileGen()
        final = game(pile)

        if final == True:
            playerwins = playerwins + 1
        elif final == False:
            computerwins = computerwins + 1
        else:
            print("\nPlayer Wins: ", playerwins, "Computer Wins: ", computerwins)
            sys.exit()

        print("\nPlayer Wins: ", playerwins, "Computer Wins: ", computerwins)
        aplay = playAgain()

    print("\nThe final score is\nPlayer Wins: ", playerwins, "Computer Wins: ", computerwins)
    sys.exit()


main()

