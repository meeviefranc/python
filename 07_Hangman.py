"""
Created on Jun 5 2022
@author: meeviefranc
"""
import random

def hangman():
    # initialize variables
    print('''
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/                       
    ''')
    hangman = ['''
          |
          |
          |
          |
          |
          |
    =========''', '''
          +
          |
          |
          |
          |
          |
    =========''', '''
      +---+
          |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    lives = 10
    got_a_letter = False
    blnk_word = []

    # generate a random word from a list
    word = ["California", "everything", "aboveboard", "Washington", "basketball", "weathering", "characters", "literature", "perfection", "volleyball",
            "depression", "homecoming", "technology", "maleficent", "watermelon", "appreciate", "relaxation", "convection", "government", "abominable",
            "salmonella", "strawberry", "aberration", "retirement", "television", "contraband", "Alzheimers", "silhouette", "friendship", "loneliness",
            "punishment", "university", "Cinderella", "confidence", "restaurant", "abstinence", "blancmange", "blackboard", "discipline", "renovation",
            "helicopter", "generation", "adaptation", "skateboard", "lightboard", "Apocalypse", "understand", "leadership", "revolution", "Antarctica"]
    rnd_word = random.choice(word)

    # display fill in the blank
    for letter in rnd_word:
        blnk_word.append("_")
    print(*blnk_word)
    while lives > 0 and "_" in blnk_word:
        # ask user to guess a letter
        user_ltr = input("Guess a letter : ").lower()
        x = 0
        if user_ltr in blnk_word:
            print("You guessed that letter already!")
            got_a_letter = False
        else:
            got_a_letter = False
            for letter in rnd_word:
                if letter == user_ltr:
                    blnk_word[x] = user_ltr
                    got_a_letter = True
                x += 1
        if not got_a_letter:
            print(f"{user_ltr} is not valid. You lost a life!")
            print(hangman[10-lives])
            lives -= 1
        print(*blnk_word)
        print(f"Number of lives left: {lives}")

    if lives == 0 and "_" in blnk_word:
        print(f"You lost! The correct word is {rnd_word}.")
    else:
        print("You won!")