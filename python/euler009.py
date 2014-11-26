#!/usr/bin/env python2
# -*- coding: utf-8 -*-

""" Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a² + b² = c²
For example, 3² + 4² = 9 + 16 = 25 = 5².
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

res = [a * b * c
       for c in xrange(0, 1000) for b in xrange(0, 500) for a in xrange(0, 330)
       if a + b + c == 1000 and a < b < c and (a*a + b*b) == c*c]

print res
