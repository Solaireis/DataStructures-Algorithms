"""
This is for Tutorial 1, Question 3
Instead of using the range step to do the counting i use bitwise operations to solve the question.
"""

def sum_of_squares1(n):
    sum = 0
    for i in range(1, n+1):
        if i & 1 == 1:
            sum += i**2
    return sum


a = int(float(input("Enter a number: ")))
numbers = (1, 2, 3, 4, 5, 6, 7)
sq = sum_of_squares1(a)
print(sq)