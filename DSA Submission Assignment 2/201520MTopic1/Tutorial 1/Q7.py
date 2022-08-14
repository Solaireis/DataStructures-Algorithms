# Write a Python function that takes a sequence of numbers 
# and determines if all the numbers are different from each other,
#  i.e. they are distinct.
# (HINT: The simple solution just checks each number against every other one,
#  but there are more efficient solutions around. For now,
#  just implement the simple solution but make sure you don’t compare a number to itself.)

def d_num(n): #currently it compares to itself 
    for i in range(len(n)):
        print('i:', n[i])
        for j in range(len(n)):
            print('data , j:', n[j])
            print('data , i:', n[i])
            if i != j: #checks if the index is comparing itself
                if n[i] == n[j]:
                    return False
        print('i:', n[i])
    return True

def distinct(data): # more efficient algo
    for k in range(1,len(data)):
        print('k:', k)
    for j in range(k):
        print('j:', j)
        print('data , j:', data[j])
        print('data , k:', data[k])
        if data[j] == data[k]:
            return False
    return True

num = [1,2,3,4,5,6,7,8,9,10,2]
num2 = [1,2,3,4,5,6,7,8,9,10,11]
print(d_num(num))
print(d_num(num2))
print(" ")
print(distinct(num))
print(distinct(num2))

#nested for loops is tested