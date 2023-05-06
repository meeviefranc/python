# -*- coding: utf-8 -*-
"""
Created on 03 May 2023
@author: meeviefranc
"""
import os
import importlib
from random import randint

art = importlib.import_module("higherlower.art")
logo = getattr(art, "logo")
game_data = importlib.import_module("higherlower.game_data")
d_dict = getattr(game_data, "data")


def choose(q, choice):
    """Validate choice for A or B"""
    ask = True
    while ask:
        ans = input(q).upper()
        if ans not in choice:
            print("Not a valid choice. Pick one: ", choice)
            ask = True
        else:
            ask = False
    return ans


def rnd_no(new_play, n2):
    """Generate random number between 0 and length of game_data to generate choices and use same celeb for option A on next round"""
    if new_play:
        n1 = randint(0, len(d_dict)-1)
    else:
        n1 = n2
    ask = True
    while ask:
        n2 = randint(0, len(d_dict)-1)
        if n2 != n1:
            ask = False
    return n1, n2


def celeb_str(c_dict):
    """format of display for name of celebs"""
    return c_dict["name"] + ", " + c_dict["description"] + ", from " + c_dict["country"] + "."


def whowins(c1, c2):
    if c1 > c2:
        winner = 'A'
    else:
        winner = 'B'
    return winner


def compare_celeb(score, celeb1, celeb2):
    """compare the no. of followers of the celebs"""
    win = False
    celeb1_dict = d_dict[celeb1]
    celeb2_dict = d_dict[celeb2]
    if score > 0:
        print(f"You're right! Current score: {score}.")
    winner = whowins(d_dict[celeb1]["follower_count"], d_dict[celeb2]["follower_count"] )
    print("Compare A: " + celeb_str(celeb1_dict))
    print(getattr(art, "vs"))
    print("Against B: " + celeb_str(celeb2_dict))
    if choose('Who has more followers? Type \'A\' or \'B\': ', ["A", "B"]) == winner:
        win = True
        score += 1
    return win, score


def higherlower():
    """main game"""
    win = new_play = True
    celeb1 = celeb2 = score = 0
    while win:
        just = os.system('clear')
        print(logo)
        celeb1, celeb2 = rnd_no(new_play, celeb2)
        win, score = compare_celeb(score, celeb1, celeb2)
        new_play = False
    print(f"Sorry, that\'s wrong. Final score: {score}")
