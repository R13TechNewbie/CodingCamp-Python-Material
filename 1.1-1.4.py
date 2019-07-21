# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#for angka_1 in range(1,5):
#        for angka_2 in range(0,angka_1):
#            print(angka_1)

#for angka_1 in range(1,5):
#    for angka_2 in range(0,angka_1):
#        print(angka_1,end=" ")
#    print("")

from tkinter import *
from tkinter import messagebox
from tkinter import Menu
#import tkinker as tk (pilih aja salah satu)

window = Tk()
window.title("Login Form")
window.geometry("600x600")

username = Label(text="Username :")
username.grid(column=0, row=0)
password = Label(text="Password :")
password.grid(column=0, row=1)

input_username = Entry()
input_password = Entry()

input_username.grid(row = 0, column = 1)
input_password.grid(row = 1, column = 1)

window.mainloop()