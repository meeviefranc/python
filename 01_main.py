# -*- coding: utf-8 -*-
"""
Created on 30 May 2022
@author: meeviefranc
"""
# clear screen - in pycharm, set run/debug config to emulate terminal in output console
import os
import importlib

# get your functions from the files
tc = importlib.import_module('02_TipCalculator')
tipcalculator = getattr(tc, "tipcalculator")
tc = importlib.import_module('03_TreasureIsland')
treasureisland = getattr(tc, "treasureisland")
tc = importlib.import_module('04_RockPaperScissors')
rockpaperscissors = getattr(tc, "rockpaperscissors")
tc = importlib.import_module('05_PwdGenerator')
pwdgenerator = getattr(tc, "pwdgenerator")
tc = importlib.import_module('07_Hangman')
hangman = getattr(tc,"hangman")
tc = importlib.import_module("08_CaesarCipher")
caesarcipher = getattr(tc,"caesarcipher")
tc = importlib.import_module("09_Auction")
auction = getattr(tc, "auction")

def display_menu():
    print('''
Notebook Menu
1. Tip Calculator
2. Treasure Island
3. Rock Paper Scissors
4. Password Generator
5. Hangman
6. Caesar Cipher
7. Auction
8. Quit Application
''')

def quit():
    print("Thank you for trying out my app!")

def chkoption():
    while True:
        try:
            opt = int(input('Type the Option Number here : '))
        except ValueError:
            print("That's not an integer!\n")
            continue
        else:
            if opt < 1 or opt > 8:
                print("Not a valid option.Type 8 to Quit. \n")
                continue
            else:
                break
    return opt


def playmore():
    ask = True
    ans = ["yes", "no"]
    while ask:
        more = input('Do you want to go back to the menu? Type \'yes\' or \'no\'. ')
        if more.lower() not in ans:
            print("Type \'yes\' or \'no\'.")
            ask = True
        else:
            ask = False
    return more.lower()


options = {1 : tipcalculator,
           2 : treasureisland,
           3 : rockpaperscissors,
           4 : pwdgenerator,
           5 : hangman,
           6 : caesarcipher,
           7 : auction,
           8 : quit,
}
play = "yes"
while play.lower() == "yes":
    just = os.system('clear')
    display_menu()
    choice = chkoption()
    just = os.system('clear')
    options[choice]()
    if choice == 8:
        play = "no"
    else:
        play = playmore()




