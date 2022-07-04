# -*- coding: utf-8 -*-
"""
Created on 13 Jun 2022
@author: meeviefranc
"""

def shift(direction,alphabet):
    new_abc = []
    x = len(alphabet)
    if direction == "left":
        for i in range(x):
            if i == 0:
                new_abc.append(alphabet[1])
            elif i == (x-1):
                new_abc.append(alphabet[0])
            else:
                new_abc.append(alphabet[i+1])
    else:
        for i in range(x-1):
            if i == 0:
                new_abc.append(alphabet[x-1])
                new_abc.append(alphabet[0])
            else:
                new_abc.append(alphabet[i])
    return new_abc

def encrypt(msg, sft, encode):
    plainalpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    alphabet = plainalpha
    j = int(sft)
    s = []
    new_msg = ""
    if encode == "encode":
        for i in range(j):
            alphabet = shift("left", alphabet)
    else:
        for i in range(j):
            alphabet = shift("right", alphabet)
    print("Here is the alphabet after the shift:\n")
    print(alphabet)
    for c in msg:
        index = plainalpha.index(c)
        s.append(alphabet[index])
    return (new_msg.join(s))

def caesarcipher():
    print ('''
     ____  ____  _____ ____  ____  ____   
    /   _\/  _ \/  __// ___\/  _ \/  __\  
    |  /  | / \||  \  |    \| / \||  \/|  
    |  \_ | |-|||  /_ \___ || |-|||    /  
    \____/\_/ \|\____\\____/\_/ \|\_/\_\  
                                          
     ____  _  ____  _     _____ ____      
    /   _\/ \/  __\/ \ /|/  __//  __\     
    |  /  | ||  \/|| |_|||  \  |  \/|     
    |  \_ | ||  __/| | |||  /_ |    /     
    \____/\_/\_/   \_/ \|\____\\_/\_\     
                                                 
           ''')

    print("Welcome to Caesar Cipher!!!\n")
    print("A slightly different approach for the original challenge.\n")
    print("This includes printing out the new alphabet after the shift.\n")

    play = "yes"
    while play.lower() == "yes":
        play = "no"
        encode = input("\n\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if (encode not in ['encode','decode']):
            print("Choose to type 'encode' or 'decode' only.")
        else:
            msg = input("Type your message:\n").lower().strip()
            if not(msg.isalpha()):
                print("Check that you have a message entered and includes only characters a to z. \n\n")
            else:
                sft = input("Type the shift number:\n")
                try:
                    val = int(sft)
                except ValueError:
                        print("That's not an integer!\n")
                else:
                    if int(sft) < 1:
                        print("Choose to shift from 1 or greater than 1 times only.\n")
                    else:
                        new_msg = encrypt(msg,sft,encode)
                        print(f"Here's the {encode}d result: {new_msg} \n\n")
                        play = input("\n\nType 'yes' if you want to go again. Otherwise type 'no': ")
                        if play.lower() == "yes":
                           print("OK! Let's cipher again!\n\n")
                        else:
                           print("You didn't say yes so oktnxbye.")
                        
        
