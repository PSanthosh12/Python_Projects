#!/usr/bin/python
print()

#README: This program will take in user input for several parts of speech and give an out of a story containing the user input

#NOTES: string concatenation methods
#foo = "" #this creates a string variable
#print("subscribe to" + foo) #basic concatentation between two strings with the + operator
#print("subscribes to {}".format(foo)) #this will format whatever the value of the variable foo is into the {}
#print(f"subscribe to {foo}") # f-string that directly lets you insert the variable into the string 

#taking in user input for parts of speech 
adjective = input("Can you give me an adjective: ")
nationality = input("Can you give me an nationality: ")
person = input("Can you give me the name of a person: ")
noun = input("Can you give me an noun: ")
adjective2 = input("Can you give me an adjective: ")
noun2 = input("Can you give me an noun: ")
adjective3 = input("Can you give me an adjective: ")
adjective4 = input("Can you give me an adjective: ")
pluralnoun = input("Can you give me an plural noun: ")
noun3 = input("Can you give me an noun: ")
number = input("Can you give me an number: ")
shapes = input("Can you give me an plural shape: ")
food = input("Can you give me a type of food: ")
food2 = input("Can you give me another type of food: ")
number2 = input("Can you give me another number: ")

#writing out the story using f-string concatenation
print()
print("Pizza Pizza MadLib!")
print()
#printing one sentence at a time is unnecssary but this way I can keep track of errors easier
print(f"Pizza was invented by a {adjective} {nationality} chef named {person}.")
print(f"To make a pizza, you need to take a lump of {noun}, and make a thin, round {adjective2} {noun2}.")
print(f"Then you cover it with {adjective3} sauce, {adjective4} cheese, and fresh chopped {pluralnoun}.")
print(f"Next you have to bake it in a very hot {noun3}.")
print(f"When is tis done, cut it into {number} {shapes}.")
print(f"Some kids like {food} pissa the best, but my favorite is the {food2} pizza.")
print(f"If I could, I would eat pizza {number2} times a day!")

#The End!
print("Thank you for playing!")
print()






