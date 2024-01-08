# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

#pseudocode
#main interface with welcome text and proceed button
first_popup = tk.messagebox.askyesno(title="Greetings!", message= "Hello! Do you want to play a game? You will give me numbers and I'll try to pick the highest number. Game?")
if first_popup == True:
    #pop up ask-int for first number
    first_number = simpledialog.askinteger("First Number", 'Please input your first number. Input "0" if you do not want to input a number.')
    #pop up ask-int for second number
    second_number = simpledialog.askinteger("Second Number", 'Please input your second number. Input "0" if you do not want to input a number.')
    #pop up ask-int for third number
    third_number = simpledialog.askinteger("Third Number", 'Please input your third number. Input "0" if you do not want to input a number.')
    #and so on can be more than 3 numbers
    fourth_number = simpledialog.askinteger("Fourth Number", 'Please input your fourth number. Input "0" if you do not want to input a number.')
    fifth_number = simpledialog.askinteger("Fifth Number", 'Please input your fifth number. Input "0" if you do not want to input a number.')
#solve using set of if-else function
if first_number > second_number and first_number > third_number and first_number > fourth_number and first_number > fifth_number:
    largest = first_number
elif second_number > first_number and second_number > fourth_number and second_number > third_number and second_number > fifth_number:
    largest = second_number
elif fourth_number > first_number and fourth_number > second_number and fourth_number > third_number and fourth_number > fifth_number:
    largest = fourth_number
elif fifth_number > first_number and fifth_number > second_number and fifth_number > third_number and fifth_number > fourth_number:
    largest = fifth_number
else:
    largest = third_number

def okay_function():
    base_window.destroy()

def descending_order_func():
    nums = [int(first_number), int(second_number), int(third_number), int(fourth_number), int(fifth_number)]
    nums.sort(reverse=True)
    tk.messagebox.showinfo(title="Descending Order", message= str(nums))
    base_window.destroy()

#show highest number, ok button and show list in descending order button
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

base_window = ctk.CTk()
base_window.title("Here is the result of my analyzation")

frame_bw = ctk.CTkFrame(base_window)
frame_bw.pack(padx= 60, pady=20)

end_label = ctk.CTkLabel(frame_bw, text=("The largest number you have inputted is: " + str(largest)), font=("sansSerif", 13))
end_label.grid(row=0, column= 0, padx=10, pady=12)

ok_button = ctk.CTkButton(frame_bw, text="Okay", command=okay_function)
ok_button.grid(row= 1, column= 0, padx=10, pady=12)

see_desc_ord = ctk.CTkButton(frame_bw, text= "See descending order", command= descending_order_func)
see_desc_ord.grid(row= 2, column= 0, padx=10, pady=12)

base_window.mainloop() 