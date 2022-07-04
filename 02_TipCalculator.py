# -*- coding: utf-8 -*-
"""
Created on 30 May 2022
@author: meeviefranc
"""


def tipcalculator():
    print("Welcome to the tip calculator.")
    tot_bill = input("What was the total bill? $")
    tip_prcnt = float(input("What percentage tip would you like to give? 10, 12 or 15? "))/100 + 1
    tot_peeps = input("How many people to split the bill? ")
    bill_tip = float(tot_bill) * tip_prcnt
    bill_split = round(bill_tip/int(tot_peeps), 2)
    print("Each person should pay: $%.2f" % bill_split)


