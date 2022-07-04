# -*- coding: utf-8 -*-
"""
Created on 02Jun2022
@author: meeviefranc
"""

import random

def pwdgenerator():
    print("Welcome to the PyPassword Generator!")
    # initialize variables
    newpwd = []
    pwd = ""
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    symbols = ['~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','|','<','>','?']
    numbers = ['0','1','2','3','4','5','6','7','8','9','0']
    # input and validation
    num_ltr = int(input("How many letters would you like in your password? "))
    if num_ltr <= 0:
        print("Input invalid - should be number greater than 0.")
    else:
        num_sym = int(input("How many symbols would you like in your password? "))
        if num_sym <= 0:
            print("Input invalid - should be number greater than 0.")
        else:
            num_num = int(input("How many numbers would you like in your password? "))
            if num_num <= 0:
                print("Input invalid - should be number greater than 0.")
    # ranges
    for n in range(1, num_ltr+1):
        rnd_int = random.choice(letters)
        newpwd.append(rnd_int)
    for n in range(1, num_sym+1):
        rnd_int = random.choice(symbols)
        newpwd.append(rnd_int)
    for n in range(1, num_num+1):
        rnd_int = random.choice(numbers)
        newpwd.append(rnd_int)
    # shuffle and create the pwd
    random.shuffle(newpwd)
    for s in newpwd:
        pwd += s
    print(f"Your new password is : {pwd}")


