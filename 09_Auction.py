# -*- coding: utf-8 -*-
"""
Created on 01 Jul 2022
@author: meeviefranc
"""

# clear screen - in pycharm, set run/debug config to emulate terminal in output console
import os


def sayhi():
    print('''
                             ___________
                             '''+'\\'+'''         /
                              )_______(
                              |"""""""|_.-._,.---------.,_.-._
                              |       | | |               | | ''-.
                              |       |_| |_             _| |_..-'
                              |_______| '-' `'---------'` '-'
                              )"""""""(
                             /_________'''+'\\'+'''
                             `'-------'`
                           .-------------.
                          /_______________'''+'\\'
          )
    print('Welcome to the secret auction program.')


def getbidamt():
    while True:
        try:
            amt = float(input('What\'s your bid?: $'))
        except ValueError:
            print("That's not an integer!\n")
            continue
        else:
            break
    return amt


def otherbids():
    ask = True
    ans = ["yes", "no"]
    while ask:
        bid = input('Are there any other bidders? Type \'yes\' or \'no\'. ')
        if bid.lower() not in ans:
            print("Type \'yes\' or \'no\'.")
            ask = True
        else:
            ask = False
    return bid.lower()


def findwin(bidders):
    winner = {}
    bid1 = 0
    for bidder in bidders:
        for bid in bidder:
            if bid1 < bidder[bid]:
                bid1 = bidder[bid]
                winner = {"name": bid, "amt": bidder[bid]}
    return winner


def collectbids():
    bidders = []
    bidder = {}
    win = {}
    bid = "yes"
    while bid.lower() == "yes":
        just = os.system('clear')
        name = input('What is your name?: ')
        amt = getbidamt()
        bid = otherbids()
        bidder = {name: amt}
        bidders.append(bidder)
    return bidders

def auction():
    sayhi()
    bidders = collectbids()
    just = os.system('clear')
    win = findwin(bidders)
    print("The winners is %s with a bid of $%.2f." % (win["name"], win["amt"]))