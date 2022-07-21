# -*- coding: utf-8 -*-
"""
Created on 11 Jul 2022
@author: meeviefranc
# some blackjack rules
# show the player's first 2 cards vs dealer's first card, e.g.:
## Your cards: [9, 10]
## Computer's first card: 8
# then ask if the player wants another card.
# show the final hands and if player won e.g.:
## Your final hand: [9, 10]
## Computer's final hand: [8, 10]
## You Win
# if dealer's 2 cards is < 17, he gets another card
# an Ace is 11 until cards are over 21, then it becomes one
"""
import os
import random


def playgame(q):
    ask = True
    ans = ["y", "n"]
    while ask:
        more = input(q)
        if more.lower() not in ans:
            print("Type \'y\' or \'n\'.")
            ask = True
        else:
            ask = False
    return more.lower()


def sayhiasc():
    print ('''
          _____
         |A .  | _____
         | /.'''+'\\'+''' ||A ^  | _____
         |(_._)|| / '''+'\\'+''' ||A _  | _____
         |  |  || '''+'\\'+''' / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || '''+'\\'+''' / |
                       |____V||  .  |
                              |____V|
     _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_'''+'\\'+''' 
                       _/ |                
                      |__/                 
    ''')


def dealcard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def checkcard():
    cards = []
    # first card
    cards.append(dealcard())
    # the next card should not be the same as the first card unless it is 10
    card = dealcard()
    while (cards[0] == card and card != 10):
        card = dealcard()
    cards.append(card)
    return cards


def anothercard(cards):
    getcard = True
    while getcard:
        card = dealcard()
        # get a card that is not yet in the deal unless it is 10
        for ccard in cards:
            if (ccard == card) and (card != 10):
                getcard = True
            else:
                getcard = False
    return card


def blackjack():
    ans = 'y'
    user_cards = []
    comp_cards = []
    while (ans == 'y'):
        ans = playgame('Do you want to play a game of Blackjack?  Type \'y\' or \'n\': ')
        if (ans == 'y'):
            just = os.system('clear')
            sayhiasc()

            user_cards = checkcard()
            comp_cards = checkcard()

            if (sum(comp_cards) < 17):
                card = anothercard(comp_cards)
                comp_cards.append(card)

            print("Your cards: %s" % user_cards)
            print("Dealer's first card: %s" % comp_cards[0])

            getcard = playgame('Type \'y\' to get another card, type \'n\' to pass: ')
            if (getcard == 'y'):
                card = anothercard(user_cards)
                user_cards.append(card)

            if sum(user_cards) > 21:
                user_cards = list(map(lambda x: 1 if x == 11 else x, user_cards))
            if sum(comp_cards) > 21:
                comp_cards = list(map(lambda x: 1 if x == 11 else x, comp_cards))

            sum_ucard = sum(user_cards)
            sum_ccard = sum(comp_cards)
            print("Your final hand: %s : %s" % (user_cards, sum_ucard))
            print("Dealer's final hand: %s : %s" % (comp_cards, sum_ccard))
            if (sum_ccard == 21):
                print("Dealer has a blackjack, You lost!")
            elif (sum_ucard > 21):
                print("Over 21, You lost!")
            elif (sum_ucard < sum_ccard) and (sum_ccard <= 21):
                print("You lost!")
            elif sum_ucard == sum_ccard:
                print("It's a draw!")
            else:
                print("You Won!")