from tkinter import *
import tkinter
import time


features = "Current features include: eggs and bread."


def intro():
    print(features, "Have fun!")

print("Welcome to calcuator by Yolian.")
intro()


num1 = input("First number?")
num1 = int(num1)
num2 = input("Second number?")
num2 = int(num2)

finalnum = num1 + num2
print ("Your number is:",finalnum)