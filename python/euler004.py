#!/usr/bin/env python

# Multiply each x (where 99 < x <= 999) by a y (where 99 < y <= 999 and
# differs from a previous x). This way, 99 * 98 and 98 * 99 won't occur.
numbers = [x*y for x in xrange(999, 99, -1) for y in xrange (999-(999-x), 99, -1)]

print max([x for x in a if str(x)[::-1] == str(x)])
