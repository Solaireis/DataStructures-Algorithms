# Modify the sum_of_squares(n) function written for Qn. 2 
# such that it now takes a positive integer n and returns 
# the sum of the squares of all the odd positive integers 
# smaller than or equal to n.

#original answer with bitwise
def sum_of_squares1(n):
    sum = 0
    for i in range(1, n+1):
        #value = i**2
        #print(value)
        if i & 1 == 1:
            sum += i**2
    return sum

#original answer with step
def sum_of_squares(n):
    sum = 0
    for i in range(1, n+1, 2):
        #value = i**2
        #print(value)
        sum += i**2
    return sum

#in tuple form
def sum_of_squares2(n):
    sum = 0
    for i in range(1, len(n)+1):
        #value = i**2
        #print("loop value" + str(value))

        if i & 1 == 1 :
            #print(i)
            sum += i**2
    return sum

a = int(float(input("Enter a number: ")))
numbers = (1, 2, 3, 4, 5, 6, 7)
sq = sum_of_squares(a)
print(sq)
sq = sum_of_squares2(numbers)
print(sq)