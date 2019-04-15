# -*- coding: utf-8 -*-
'''
Created on Tue Oct  3 01:45:55 2017

@author: TempAdmin1
'''

def f(x):
    return 9 - x*(x-10)

def fprime(x):
    return -2*x +10

guess = 10

for val in range(1, 10):
    nextGuess= guess - f(guess)/fprime(guess)
    print(nextGuess)
    guess =nextGuess