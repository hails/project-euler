#!/usr/bin/env python

x = 0
y = 1
seq = []

while x < 4000000:
    z = x + y
    x = y
    y = z
    seq.append(x)

print sum([a for a in seq if a % 2 == 0])