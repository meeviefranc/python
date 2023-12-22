# -*- coding: utf-8 -*-
"""
Created on Jun  3 16:32:12 2022
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
@author: meeviefranc
"""

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    while wall_in_front():
        turn_left()
    move()
    while wall_on_right() and not at_goal():
        if front_is_clear():
            move()
        else:
            turn_left()
    while wall_in_front() and not at_goal():
        if right_is_clear():    
            turn_right()
        else:
            turn_left()
    move()
    while not wall_in_front() and not at_goal():
        move()
    if wall_in_front() and wall_on_right():
        turn_left()
    else:    
        turn_right()
    move()

while not at_goal():
    if front_is_clear(): 
        move()  
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front():
        jump()
    else:
        turn_right()