# Title: largest palindrome product
# Description: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Goal: Find the largest palindrome made from the product of two 3-digit numbers.

def ispalin(N):
    x = str(N)
    if x == x[::-1]:
        return True
    return False

def p4():
    largest_palin = 1
    for index in range(100, 1000):
        for p in range(100, 1000):
            if index * p > largest_palin:
                if ispalin(index * p):
                    largest_palin = index * p
    print(largest_palin)