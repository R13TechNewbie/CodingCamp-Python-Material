#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:38:53 2019

@author: root
"""
from functools import partial
from tkinter import *
from tkinter import messagebox
from tkinter import Menu
import sign_up as su

toolbar_list=(('Home','Contact Us', 'Help'),(
              ('Login','Sign Up'),
              ('Contact','Security'),
              ('About','Forum')))

def toolbar(window):
    list_page_all=[]
    menu=Menu(window)
    for kunci in range(len(toolbar_list[0])):
        list_page_all.append(Menu(menu))
        for kunci2 in range(len(toolbar_list[1][kunci])):
            list_page_all[kunci].add_command(label=toolbar_list[1][kunci][kunci2])
        menu.add_cascade(label=toolbar_list[0][kunci],menu=list_page_all[kunci])
    window.config(menu=menu)
    
#    menu=Menu(window)
#    list_page=Menu(menu)
#    list_page.add_command(label='Login')
#    list_page.add_separator()
#    list_page.add_command(label='Sign Up')
#    menu.add_cascade(label='Page',menu=list_page)
#    
#    list_opt=Menu(menu)
#    list_opt.add_command(label='check version')
#    list_opt.add_separator()
#    list_opt.add_command(label='forgot password')
#    menu.add_cascade(label='Option',menu=list_opt)
#    window.config(menu=menu)
    
window = Tk()
window.title("Sign Up Form")
toolbar(window)
window.geometry("600x600")
su.layout(window)

window.mainloop()