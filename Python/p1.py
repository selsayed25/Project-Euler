# Title: 
# Description: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Goal: Find the sum of all the multiples of 3 or 5 below 1000.

sum = 0

for index in range(1, 10):
    if index % 3 == 0 or index % 5 == 0:
        sum += index

print(sum)