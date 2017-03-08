#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 21:57:55 2017

@author: Theo
"""

# The collatz sequence sometimes called the simpliest
# implossible math problem.
# The user is asked to enter a number.
# Then if the number is even, it's divided by 2.
# Else it is mutiplied by 3 and 1 is added.
# This procedure is repeated by the same rule
# until it stopsl



def collatz(number):
    n = int(number)
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(n)
    if n==1:
        return # automatically returns None
    else:
        return collatz(n)

while True:
    print("Give a number:", end=": ")
    try:
        number = int(input())
        break
    except ValueError:
        print("This input was not a number.")

collatz(number)

spam = ['spooky', 'fat tail', 'red']
def printCats(spam):
    for item in spam[:-1]:
        print(item + ',', end=" ")
    print('and ' + spam[-1])


