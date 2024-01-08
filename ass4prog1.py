# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

#pseudocode
#main interface with welcome text and proceed button
first_popup = tk.messagebox.askyesno(title="Greetings!", message= "Hello! Do you want to play a game? You will give me numbers and I'll try to pick the highest number. Game?")
if first_popup == True:
    first_number = simpledialog.askinteger("First Number", "Please input your first number")
    second_number = simpledialog.askinteger("Second Number", "Please input your second number")
    third_number = simpledialog.askinteger("Third Number", "Please input your third number")
    print (first_number, second_number, third_number)
#pop up ask-int for first number 
#first_number = int(input("Enter your first number: "))
    
#pop up ask-int for second number
#second_number = int(input("Enter your second number: "))
    
#pop up ask-int for third number
#third_number = int(input("Enter your third number: "))
    
#and so on can be more than 3 numbers
#store ng data sa variables
    
#solve using set of if-else function
#if first_number > second_number and first_number > third_number:
    #largest = first_number
#elif second_number > first_number and second_number > third_number:
    #largest = second_number
#else:
    #largest = third_number

#show highest number, ok button and show list in descending order button
# if ok then end if latter then new pop up showmessage with ok only button
#remove existing data   