# Title: Largest prime number
# Description: The prime factors of 13195 are 5, 7, 13 and 29.
# Goal: What is the largest prime factor of the number 600851475143?

import math

def main():
    s = 600851475143

    while True:
        spf = smallPrime(s)
        if spf < s:
            s //= spf
        else:
            return str(s)

def smallPrime(n):
    assert n >= 2
    for index in range(2, math.sqrt(n) + 1):
        if n % index == 0:
            return index
    return n