# -*- coding: utf-8 -*-
"""
Created on 30 May 2022
@author: meeviefranc
"""


def sayhi():
    """print ascii art for calculator"""
    print('''
     __________
    | ________ |
    ||12345678||
    |""""""""""|
    |[M|#|C][-]|
    |[7|8|9][+]|
    |[4|5|6][x]|
    |[1|2|3][%]|
    |[.|O|:][=]|
     __________
        ''')


def chkno(numName):
    """validate if input is a number"""
    q = 'What\'s the ' + numName + ' number?: '
    while True:
        try:
            num = int(input(q))
        except ValueError:
            print("That's not an integer!\n")
            continue
        else:
            break
    return num


def chkop():
    """validate if operator from input is valid"""
    ask = True
    ans = ["+", "-", "*", "/"]
    while ask:
        op = input('Pick an operation: ')
        if op not in ans:
            print("Not in the operation list. Try again. ")
            ask = True
        else:
            ask = False
    return op


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def operate(firstNo, op, nextNo):
    """perform selected calculations"""
    operations = {'+': add,
                  '-': subtract,
                  '*': multiply,
                  '/': divide,
                 }
    return operations[op](firstNo, nextNo)


def chkcon(ans):
    """validate if response is y or n"""
    ask = True
    yn = ["y", "n", "q"]
    q = 'Type \'y\' to continue calculating with ' + ans + ', or type \'n\' to start a new calculation: '
    while ask:
        resp = input(f"Type \'y\' to continue calculating with {ans} or type \'n\' to start a new calculation. Type \'q\' to exit : ")
        if resp not in yn:
            print("y or n only... Try again. ")
            ask = True
        else:
            ask = False
    return resp


def calculator():
    sayhi()
    firstNo = chkno("first")
    print('+\n-\n*\n/')
    con = 'y'
    while con == 'y':
        op = chkop()
        nextNo = chkno("next")
        if op == '/' and nextNo == 0:
            print("I cannot divide anything with 0!")
            ans = 0
        else:
            ans = operate(firstNo, op, nextNo)
        print("%.2f %s %d = %.2f" %(firstNo, op, nextNo, ans))
        con = chkcon(str(ans))
        firstNo = ans
    if con == 'n':
        calculator()


