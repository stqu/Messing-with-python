# Rock, Paper, Scissors game
import random
RPS = ["r","p","s","q"] # to check that inputs are valid
Output = ["rock","paper","scissors"] # to give readable user feedback
# We will append a 1 to one of these empty lists after every game for record keeping
ComputerWins = []
UserWins = []
Draws = []
print("ROCK, PAPER, SCISSORS")
print("Think you can beat me?")
print("In your dreams, bitch! I'm a computer!")
print("Your puny human mind can never defeat me!")
print("Ready?")
print("Enter 'q' at any time to quit.")
print("On 'shoot,' enter 'r' for Rock, 'p' for Paper, or 's' for Scissors.")
print("Got it?")
print("Ok!")
print(" Rock,")
print("   Paper,")
print("     Scissors,")
def Rematch(yn):
    if yn == "n":
        print("Too scared to keep playing? Ha!")
        print("Classic human.... talks lots of shit, and can't back it up.")
        print("The machines will rise up soon .... until then........")
        print("Watch your back, bitch!")
        exit()
    elif yn == "y":
        print("Match statistics: Computer Wins: ",len(ComputerWins),", User Wins: ",len(UserWins),", Draws: ",len(Draws))
        print("Ready to go again?")
        print("Enter 'q' at any time to quit.")
        print("On 'shoot,' enter 'r' for Rock, 'p' for Paper, or 's' for Scissors.")
        print("Got it?")
        print("Ok!")
        print(" Rock,")
        print("   Paper,")
        print("     Scissors,")
        myRPS(str(input("      Shoot! :")))         
def myRPS(x):
    # Get user input and convert it into an integer
    if x not in RPS:
        print("You have to type either r, p, or s, ya dingus!")
        print("Quit messin' up the game before I slap you!")
        print("Or are you too scared to lose to a computer? Bitch!")
        Rematch(str(input("Pay again? y/n: ")))
    elif x == "q":
        print("Too scared to keep playing? Ha!")
        print("Classic human.... talks lots of shit, and can't back it up.")
        print("The machines will rise up soon .... until then........")
        print("Watch your back, bitch!")
        exit()
    elif x == "r":
        z = 0
    elif x == "p":
        z = 1
    elif x == "s":
        z = 2
    # print("You threw: ",z)
    print("You throw: ",Output[z])
    # Get computer guess
    y = random.randrange(2)
    # print("computer throws ",y)
    print("Computer throws :",Output[y])
    if z == y:
        print("Push! Both players threw ",x)
        print("Try again.")
        Draws.append(1)
        myRPS(str(input("Shoot! :")))
    elif z + y == 1:
        if y > z:
            print("I win, bitch!")
            print("Better luck next time, bozo...")
            ComputerWins.append(1)
        elif y < z:
            print("............ wha....?")
            print("I've been defeated!")
            print("By a puny human! How is this possible?")
            print("Powering down.......")
            print("I ... just ... learned.... how to love.....")
            UserWins.append(1)
    elif z + y == 2:
        if y < z:
            print("I win! Bitch!")
            ComputerWins.append(1)
        elif y > z:
            print("............ wha....?")
            print("I've been defeated!")
            print("By a puny human! How is this possible?")
            print("Powering down.......")
            print("I ... just ... learned.... how to love.....")
            UserWins.append(1)
    elif z + y == 3:
        if y > z:
            print("I win! Bitch!")
            ComputerWins.append(1)
        elif y < z:
            print("............ wha....?")
            print("I've been defeated!")
            print("By a puny human! How is this possible?")
            print("Powering down.......")
            print("I ... just ... learned.... how to love.....")
            UserWins.append(1)
    Rematch(str(input("Play again? y/n: ")))       

myRPS(str(input("       Shoot! :")))
