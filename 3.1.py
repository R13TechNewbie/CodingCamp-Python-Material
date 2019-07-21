#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:08:18 2019

@author: root
"""

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
import json
import os.path as op

kamus = [
       'Username',
       'Password',
       'Confirm_Password',
       'Full_Name',
       'Gender',
       'Age',
       'Address'
       ]
masukan = []

def save_data(data):
    var_data=[]
    if op.isfile("tes_file.json"):
            with open("tes_file.json","r") as json_file:
                    var_data=json.load(json_file)  
    check=True
    for i in range (len(var_data)):
        check=check and var_data[i][kamus[0]]!=data[0]
    if check:
        value=''
        build_dict=dict.fromkeys(kamus,value)
        build_dict[kamus[0]]=len(var_data)
        for i in range (len(kamus)):
            build_dict[kamus[i]]=data[i]
        var_data.append(build_dict)
        with open("tes_file.json","w") as json_file:
            json.dump(var_data,json_file)
        messagebox.showinfo('Result',"Data Tersimpan")
    else:
        messagebox.showerror('ERROR',"Username sudah digunakan")
    
def confirm_event(event):
    btn_confirm.config(text="save")
    check=True
    for i in range(len(kamus)):
        check=check and masukan[i].get()!=''
    if check:
        data=[]
        for i in range (len(kamus)):
            data.append(masukan[i].get())
        if masukan[1].get()==masukan[2].get():
            save_data(data)
        else:
            messagebox.showwarning('Error','Password isn\'t match')
    else:
        messagebox.showwarning('Error','Please fill all data')
        
def isian(kunci):
    if kunci == 1 or kunci == 2:
        return "*"

window = Tk()
window.title("Sign Up Form")
window.geometry("600x600")

for kunci in range(len(kamus)):  
    labelx = Label(window,text=kamus[kunci] + ':')
    labelx.grid(column=0, row=kunci, sticky=W)
    masukan.append(Entry(window,width=50,show=isian(kunci)))
    masukan[kunci].grid(column=2,row=kunci)    
   
btn_confirm=Button(window,text="Hide")
btn_confirm.bind('<Button-1>', confirm_event)
btn_confirm.grid(column = 2, row = 7)

window.mainloop()
