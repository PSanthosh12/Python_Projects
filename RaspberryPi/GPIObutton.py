#!/usr/bin/python

#README: This program takes in an external input (the pressing of a button) and prompts an internal output (printing "You did it!")

#importing the Raspberry Pi GPIO library and calling it GPIO
import RPi.GPIO as GPIO

#telling the GPIO to ignore warnings for now
GPIO.setwarnings(False)

#indicate you want GPIO to recognize and use physical pin numbers so that we can indicate which pin the button is attached to
GPIO.setmode(GPIO.BOARD)

#setting the active input pin as 10 and set the initial value to be low(off)
#when current flows through the pin, it will become high(on) and trigger the program 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD.DOWN)
#10 = the thing attached to pin 10 (this should be the hot pin, not the grounding one)
#GPIO.IN = this defines the given pin (10) as the input pin
#pull_up_down = this sets the initial value (the up down property) of the pin as DOWN (off)

#create a loop that continuously reads the port and outputs a message when the button is pressed (when the pin is triggered by being high/ turned on)
while True:  #the while loop that reads the input
    if GPIO.input(10) == GPIO.HIGH:  #if the button is pressed (becomes high, which means electricity flows through it, turning it on)
        print("You did it!") #then do this (print the string)
