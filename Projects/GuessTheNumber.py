#!/usr/bin/python

#README: This program will work with Python's random module, build functions, work with while loops and conditionals, and get user input
print()

#first we need to import the random module from thePython library for us to use
import random #random module documentation: https://docs.python.org/3/library/random.html


#COMPUTER VERSION: The computer generates a random number that the user is trying to guess

#define a function that generates the random integer
def guess(x):
    random_number = random.randint(1,x) #the randint(a.b) command is from the random module that generates a random integer within the range (a,b)
    guess = 0 #just initializing the variable guess so that python does't set it equal to the random_number
    #create a while loop that takes in user guesses, tells if it's too high, too low, or the user guess correctly
    while guess != random_number: #if the gues DOES NOT equal the random_number
        guess = int(input(f"Guess a number between 1 and {x}: "))
        print()
        if guess < random_number: #if the guess is too low
            print(f"Sorry {guess} is too low! Guess again.")
            print()
        elif guess > random_number: #if the guess is too high
            print(f"Sorry {guess} is too high! Guess again.")
            print()
    print(f"Congrats! You guessed the right number!")
    print()

#define the parameter for the guess (what x in guess(x) is)
guess(100) 
#the computer will generate a number between 1 and 10
#the user will also be prompted to pick a number between 1 and 10

#The End!
print("Thank you for playing!")
print()



#USER VERSION: The user has a number and the computer has to try and guess it

#define a function 
def computer_guess(x):
    #continue tutorial from 13:50
