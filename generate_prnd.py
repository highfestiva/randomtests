#!/usr/bin/env python3

'''Generates a short file containing pseudo-random numbers from the random library.'''

import random

digits_per_line = 25
lines = 5000
maxdigit = 2**digits_per_line-1

f = open('data.prnd.txt', 'w')
for _ in range(lines):
    num = random.randint(0,maxdigit)
    for _ in range(digits_per_line):
        print(str(num&1), end='', file=f)
        num = num >> 1
    print(file=f)
