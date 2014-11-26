#!/usr/bin/env python 2
# -*- encoding: utf-8 -*-

""" Problem 5
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

def is_evendiv(number):
    for num in xrange(1, 21):
        if number%num != 0:
            return False
    return True


start = 20
while(not is_evendiv(start)):
    start += 20

print start
