# -*- coding: utf-8 -*-
"""
Created on Fri May 17 22:34:37 2024

@author: Diego Emmanuel C Cordero
"""

from random import choice

num=0

while num==0:
    game=["ROCK","PAPER","SCISSOR"]
    computer_player=choice(game)
    player_input=input("Type your choice between ROCK, PAPER, SCISSORS (use capital letters only) type 0 to exit:")
    if player_input==0:
        print("Thank you for playing")
        break
    print("Computer Answer:", computer_player)
    
    if player_input=="PAPER" and computer_player=="PAPER":
        print("DRAW")
    elif player_input=="PAPER" and computer_player=="ROCK":
        print("YOU WIN")
    elif player_input=="PAPER" and computer_player=="SCISSORS":
        print("YOU LOSE")     
    elif player_input=="ROCK" and computer_player=="ROCK":
        print("DRAW")
    elif player_input=="ROCK" and computer_player=="PAPER":
        print("YOU LOSE")
    elif player_input=="ROCK" and computer_player=="SCISSORS":
        print("YOU WIN") 
    elif player_input=="SCISSORS" and computer_player=="SCISSORS":
        print("DRAW")
    elif player_input=="SCISSORS" and computer_player=="ROCK":
        print("YOU LOSE")
    elif player_input=="SCISSORS" and computer_player=="PAPER":
        print("YOU WIN")
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            