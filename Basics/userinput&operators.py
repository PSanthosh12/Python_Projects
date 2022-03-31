#!/usr/bin/python

#README: This program will take in user input (numbers) and run them through operators and return the modified values

print() #extra line for the aesthetic

#taking in user input
num1 = int(input("Please give me a number: "))
num2 = int(input("Please give me another number: "))
#int() = all user inputs always come in as strings and you can't do math with strings so you need to CAST them as integers

#creating operator commands
add = num1 + num2 #adding the two inputs
sub = num1 - num2 #subtracting the two inputs
mul = num1 * num2 #multiplying the two inputs 
div = num1 / num2 #dividing the two inputs: / is float (not rounded) and // is floor (rounded)
mod = num1 % num2 #modifying the two inputs: dividing the two inputs and finding the remainder

#printing the math
print() #extra line for the aesthetic
print(add) 
print(sub)
print(mul)
print(div)
print(mod)
print() #extra line for the aesthetic