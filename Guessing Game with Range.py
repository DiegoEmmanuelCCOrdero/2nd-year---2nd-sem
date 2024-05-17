# -*- coding: utf-8 -*-
"""
Created on Fri May 17 21:45:13 2024

@author: Diego Emmanuel C Cordero
"""

import random

maxn = 20
n = random.randint(1, maxn)

print("This program is a guessing game! There are only 3 chances to play this game.")


for i in range(3):
    guess=eval(input("Type your guess number between 1 and 20: "))
    if guess < n:
        print("your guess was too low")
        guess = guess + 1
    elif guess > n:
        print("your guess was too high")
        guess = guess + 1
    elif guess == n:
        print("Congratulations, You got it! ")
    else:
        print("Oops wrong! Please try again.")
       
print("")
print("Game over!")
print("the random number is:" ,n )