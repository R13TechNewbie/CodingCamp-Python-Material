#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:39:27 2019

@author: root
"""

import json
import os.path as op

var_data=[]
if op.isfile("tes_file.json"):
        with open("tes_file.json","r") as json_file:
                var_data=json.load(json_file)  
key=("id","first name","last name","title","school email", "phone", "school name", "school address")
value=''
build_dict=dict.fromkeys(key,value)
build_dict[key[0]]=len(var_data)+1
for i in range (1,len(key)):
    build_dict[key[i]]=input("your "+key[i]+" : ")
var_data.append(build_dict)
with open("tes_file.json","w") as json_file:
    json.dump(var_data,json_file)