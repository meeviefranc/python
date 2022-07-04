# -*- coding: utf-8 -*-
"""
Created on 01Jun2022
@author: meeviefranc
"""

import random

def rockpaperscissors():
    # initialize variables
    rock = ''' ROCK
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''
    paper = ''' PAPER
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''
    scissor = ''' SCISSOR
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    hand_image = [rock, paper, scissor]

    # get the choice of the human
    human = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
    if (human >= 0) and (human < 3):
        print(hand_image[human])
        # get the choice of the computer
        computer = random.randint(0,2)
        print("computer chose: ")
        print(hand_image[computer])

        # evaluate game result
        if human == computer:
            print("It's a TIE!")
        elif (human == 0 and computer == 2) or (human == 1 and computer == 0) or (human == 2 and computer == 1):
            print("CONGRATS, you win!")
        else:
            print("You LOST!")
    else:
        print("Invalid input - please type 0 or 1 or 2.")


