# This is a game where the program will generate a random number between
# 1 and 20. The user has to guess what the computer has picked.
# If the guess was correct, the user wins.
# If wrong, the computer gives a hint: if the guess was too high or too low.
# Total number of guesses will be displayed at the end.

print("Guessing game!")
print("The computer will pick a number between 1 and 20.")
print("Try to guess it!")
print("The computer will give you feedback if your guess is wrong")
print("Generating random number...")
print("...........................")
print("...........................")
print("Done!")
import random
guessList = []
x = random.randrange(1, 20)
# uncomment next line for testing
# print(x)
g1 = int(input("Enter your guess: "))
guessList.append(g1)
if g1 == x:
    print("SWISH! Nailed it on the first try")
    print("You had a total of",len(guessList),"guesses")
    print("Badass!")
    exit()
elif g1 < x:
    print("Too low! Guess again.")
elif g1 > x:
    print("Too high! Guess again.")
g2 = int(input("Enter your second guess: "))
guessList.append(g2)
print("Your guesses so far: ",guessList)
if g2 == x:
    print("BOOYAH! Nailed it on the second try")
    print("Badass!")
    exit()
elif g2 < x:
    print("Too low! Guess again.")
elif g2 > x:
    print("Too high! Guess again.")
    
def myFunction(y):
    guessList.append(y)
    if y == x:
        print("Correct. Finally! Took you long enough.")
        print("You made a total of ",len(guessList)," guesses.")
        print("Better luck next time, Bozo.")
        exit()
    elif y < x:
        print("Too low! Guess again.")
        print("Your guesses so far: ",guessList)
    elif y > x:
        print("Too high! Guess again.")
        print("Your guesses so far: ",guessList)
    myFunction(int(input("Enter your guess: ")))

myFunction(int(input("Enter your guess: ")))
