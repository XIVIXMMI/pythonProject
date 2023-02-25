import math
import os
import random
import re
import sys

#Task
# Given an integer, n, perform the following conditional actions:
#   If n is odd, print Wei rd
#   If n is even and in the inclusive range of 2 to 5, print Not Weird
#   If n is even and in the inclusive range of 6 to 20, print Wei rd
#   If n is even and greater than 20, print Not Weird



n = int(input().strip())

if n % 2 == 1:
    print("Weird")
elif n in range(2, 6):
    print("Not Weird")
elif n in range(6, 21):
    print("Weird")
else:
    print("Not Weird")
