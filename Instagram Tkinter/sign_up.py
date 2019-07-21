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
from init import *

masukan = []

def show():
    body.pack()

def hide():
    body.pack_forget()

def layout(window):
    body=Frame(window)
    body.pack(fill=Y)
    for kunci in range(len(kamus)):  
        labelx = Label(body,text=kamus[kunci] + ':')
        labelx.grid(column=0, row=kunci, sticky=W)
        masukan.append(Entry(body,width=50,show=isian(kunci)))
        masukan[kunci].grid(column=2,row=kunci)    
       
    btn_confirm=Button(body,text="Hide")
    btn_confirm.bind('<Button-1>', partial(confirm_event,masukan))
    btn_confirm.grid(column = 2, row = 7)