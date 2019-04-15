# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 02:43:39 2017

@author: TempAdmin1
"""

def add1(x): return x + 1

def call_fun(f, x):
    return f(x)

def add(x, y):
    return x + y

def call_fun2(f, x, y):
    return f(x, y)

def square(x):
    return x * x

def cube(x): return x * square(x)

def f1(x):
    return cube(x)- 2 * x - 5

def fprime(x): 
    return 3 * square(x) - 2

def f2(x): 
    return cube(x) * cube(x) - 2

def fprime2(x):
    return 6 * cube(x) * square (x)



def newton_raphson (x, f, fprime):
    guess = 10
    for val in range(1, 1000):
        nextGuess= guess - f(guess)/fprime(guess)
    print(nextGuess)
    guess = nextGuess