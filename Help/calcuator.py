from tkinter import *
import tkinter
import time


features = "Current features include: Combining two numbers or subtracting two numbers."

def intro():
    print(features, "Have fun!")

def func_subtract():
    num1 = input("First number? ")
    num2 = input("Second number? ")
    num1 = int(num1)
    num2 = int(num2)
    global finalnum
    finalnum = num1 - num2

def func_add():
    num1 = input("First number? ")
    num2 = input("Second number? ")
    num1 = int(num1)
    num2 = int(num2)
    global finalnum
    finalnum = num1 + num2


print("Welcome to calcuator by Yolian.")
intro()

choice1 = input("Would you like to subtract or add?")

if choice1 == "subtract":
    func_subtract()
elif choice1 == "Subtract":
    func_subtract()
elif choice1 == "add":
    func_add()
elif choice1 == "Add":
    func_add()
else: print("I don't undertsand that")

global finalnum
print ("Your final number is:",finalnum)