#!/usr/bin/env python 2
# -*- encoding: utf-8 -*-

""" Problem 7
By listing the first six prime numrs: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.
What is the 10 001st prime number?
"""

from math import sqrt

def is_prime(number):
    for x in xrange(2, int(sqrt(number)) + 1):
        if number % x == 0:
            return False
    return True

number = 2
primes = []
while(len(primes) <= 10000):
    if is_prime(number):
        primes.append(number)
    number += 1

print primes[10000]
