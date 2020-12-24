# Task
# Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20 , print Not Weird
# Input Format

    # A single line containing a positive integer, n .

# Constraints 1<= n <= 100

# Output Format

    # Print Weird if the number is weird. Otherwise, print Not Weird.


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

if (n in range(6,21) or n % 2 != 0):
    print('Weird')
else:
    print('Not Weird')

# The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

# This one is really straightforward but you can get this all on one line and use the sep = '\n' to create seperation

print((a + b), (a - b), (a * b), sep='\n')

