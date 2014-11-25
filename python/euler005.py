#!/usr/bin/env python


def is_evendiv(number):
    for num in xrange(1, 21):
        if number%num != 0:
            return False
    return True


start = 20
while(not is_evendiv(start)):
    start += 20

print start
