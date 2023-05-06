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
    ask = True
    while ask:
        ans = input(q)
        if ans not in choice:
            print("Not a valid choice. Pick one: ", choice)
            ask = True
        else:
            ask = False
    return ans


def rnd_no():
    n1 = randint(0, len(d_dict))
    ask = True
    while ask:
        n2 = randint(0, len(d_dict))
        if n2 != n1:
            ask = False
    return n1, n2


def celeb_str(c_dict):
    return c_dict["name"] + ", " + c_dict["description"] + ", from " + c_dict["country"] + "."


def compare_celeb(score):
    win = False
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    celeb1, celeb2 = rnd_no()
    celeb1_dict = d_dict[celeb1]
    celeb2_dict = d_dict[celeb2]
    celeb1_flw = d_dict[celeb1]["follower_count"]
    celeb2_flw = d_dict[celeb2]["follower_count"]
    if celeb1_flw > celeb2_flw:
        winner = 'A'
    else:
        winner = 'B'
    print("Compare A: " + celeb_str(celeb1_dict))
    print(getattr(art, "vs"))
    print("Against B: " + celeb_str(celeb2_dict))
    if choose('Who has more followers? Type \'A\' or \'B\': ', ["A", "B"]) == winner:
        win = True
        score += 1
    return win, score


def higherlower():
    win = True
    score = 0
    while win:
        just = os.system('clear')
        win, score = compare_celeb(score)
    print(f"Sorry, that\'s wrong. Final score: {score}")
