#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 13:43:49 2019

@author: root
file ketiga
"""
from tkinter import *
from tkinter import messagebox
from tkinter import Menu

kamus = [
       'Username',
       'Password',
       'Full_Name',
       'Gender',
       'Age',
       'Address',
       'apa',
       'lagi'
       ]

window = Tk()
window.title("Sign Up Form")
window.geometry("600x600")

for kunci in range(len(kamus)):    
    labelx = Label(text=kamus[kunci] + ':')
    labelx.grid(column=0, row=kunci, sticky=W)
    rw = rw + 1
    
    nama_textbox = 'textbox' + str(kunci+1)
    textboxx = Entry()
    textboxx.grid(row = kunci, column = 1, sticky=E)
    
window.mainloop()
