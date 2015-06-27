#!/usr/bin/python3
#
# A program that models the Rock-paper-scissors-lizard-Spock game
#
# by: Francis Kessie
#     
# 
"""
The key idea of this program is to equate the strings
 "rock", "paper", "scissors", "lizard", "Spock" to numbers as follows:
0 - rock
1 - Spock
2 - paper
3 - lizard
4 - scissors
In this expanded list, each choice wins against the preceding two choices 
and loses against the following two choices (if rock and scissors are thought 
of as being adjacent using modular arithmetic
"""

import random

def name_to_number(name):
    """function that converts name to number"""
    name = name.lower()
    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return(2)
    elif name == "lizard":
        return(3)
    elif name == "scissors":
        return(4)
    else:
        return "input name is invalid"


def number_to_name(number):
    """function that convers number to name"""
    if number == 0:
        return "rock"
    elif number == 1:
        return "spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "input number is invalid"  
        

def rpsls(player_choice):
    """
    Takes as input, player choice, generates a random choice for 
    computer and makes computations to determine the winner
    """    
    print()
    player_number = name_to_number(player_choice)
    print("Player choses", player_choice)
    
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print("Computer chooses", comp_choice) 
    
    winning_number = (comp_number - player_number) % 5
    if comp_number == player_number:
        print("No winner, there is a tie")
    elif winning_number <= 2:
        print("Computer wins") 
    else: 
        print("Player wins")
    
# test for code  
options = ["rock", "spock", "paper", "lizard", "scissors"]
if __name__ == "__main__":
    while True:      
            inp = input("Select one ("+ ", ".join(options) + " (or press enter to quit):")
            if not inp:
                break
            elif inp.lower() not in options:
                print()
                print("invalid selection")
            else:
                try:
                    rpsls(inp)
                except TypeError:
                    print()
                    print("invalid input")
                    continue
    
