#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

""" Problem 4
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

numbers = [x*y for x in xrange(999, 99, -1) for y in xrange (999-(999-x), 99, -1)]

print max([x for x in numbers if str(x)[::-1] == str(x)])
