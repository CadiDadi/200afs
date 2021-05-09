# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 

# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
# Read below for tips:

# Random Numbers (and Modules)
# This is your first exposure to using Python code that somebody else wrote. In Python, these formally-distributed code packages are called modules. The thing we want from a module in this exercise is the ability to generate random numbers. This comes from the random module.

# To use a module, at the top of your file, type
#      import random
# This means you are allowing your Python program to use a module called random in the rest of your code.
# To use it (and generate a random integer), now type:
#      a = random.randint(2, 6)
# Once you run this program, the variable a will have a random integer that the computer made for you, between 2 and 6 (including 2 and 6). The specific documentation for this method is here (Links to an external site.).

# There are many ways you can generate random numbers - integers, decimals, and much more. The Python documentation (Links to an external site.) has much more detailed information about what is possible from the random module.

import random 

guesses = 0 
a = random.randint(1, 10)
print("This is the RANDOM GUESSING GAME! At any time, you may type '000' to stop playing.")
print("The computer has generated a number between 1 and 10")
while guesses < 9:
    print("What is your guess?")
    guess = input()
    guess = int(guess)
    guesses = guesses + 1 
    if guess == 000:
        print("Chicken, you are scared to lose!")
        break
    if guess > a:
        print("Sorry, that's too HIGH, try again")
    if guess < a: 
        print("Sorry, that's too LOW, try again")
    if guess == a: 
        break 
if guess == a:
    guesses = str(guesses)
    print("Congrats, you got it!")
    print("Superstar! you guessed it in only ", guesses, " tries.")


