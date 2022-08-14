# Write a short Python function sum_of_squares(n)
#  that takes a positive integer n and 
# returns the sum of the squares of 
# all the positive integers smaller than or equal to n.

#original answer
def sum_of_squares(n):
    sum = 0
    for i in range(1, n+1):
        value = i**2
        print(value)
        sum += i**2
    return sum

#if test code given is a list
def sum_of_squares2(n):
    sum = 0
    for i in range(1, len(n)+1):
        value = i**2
        print(value)
        sum += i**2
    return sum

#test code
a = int(float(input("Enter a number: ")))
numbers = (1, 2, 3, 4, 5, 6, 7)
sq = sum_of_squares(a)
print(sq)
sq = sum_of_squares2(numbers)
print(sq)