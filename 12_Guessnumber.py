# -*- coding: utf-8 -*-
"""
Created on 21 Jul 2022
@author: meeviefranc
"""
import os
from random import randint


def sayhi():
    print('''
   ______                        __  ___         _   __                __                 
  / ____/_  _____  __________   /  |/  /_  __   / | / /_  ______ ___  / /_  ___  _____    
 / / __/ / / / _ \/ ___/ ___/  / /|_/ / / / /  /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/    
/ /_/ / /_/ /  __(__  |__  )  / /  / / /_/ /  / /|  / /_/ / / / / / / /_/ /  __/ /        
\____/\__,_/\___/____/____/  /_/  /_/\__, /  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/         
                                    /____/                                                
    ''')


def choose(q, choice, game):
    ask = True
    while ask:

        if game:
            while True:
                try:
                    ans = int(input(q))
                except ValueError:
                    print("That's not an integer!\n")
                    continue
                else:
                    break
        else:
            ans = input(q).lower()

        if ans not in choice:
            print("Not a valid choice. Pick one: ", choice)
            ask = True
        else:
            ask = False
    return ans


def guessnumber():
    just = os.system('clear')
    sayhi()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    think = randint(0, 100)
    ans = choose('Choose a difficulty. Type \'easy\' or \'hard\': ', ["easy", "hard"], False)
    if ans == 'easy':
        guess = 10
    else:
        guess = 5
    win = False
    attempt = guess
    while attempt <= guess and attempt != 0:
        if attempt != guess:
            print("Guess again.")
        print(f'You have {attempt} attempts remaining to guess the number.')
        player = choose('Make a guess :', list(range(1, 101)), True)
        if player == think:
            print("You got it! ")
            win = True
            attempt =0
        else:
            attempt -= 1
            if player > think:
                print("Too high.")
            else:
                print("Too low.")
    if win:
        print(f"The answer was {think}!")
    else:
        print("You\'ve run out of guesses, you lose.")