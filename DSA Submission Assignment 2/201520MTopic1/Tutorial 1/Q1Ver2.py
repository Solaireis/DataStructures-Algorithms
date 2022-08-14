# Complete the following Python function,
#  minmax(data)such that it takes a sequence of one or more numbers,
#  and returns the smallest and largest numbers, in the form of a tuple of length two.
# (NOTE: Do not use the built-in min or max in implementing your solution.)

#Alternative solution for qn 1

def minmax(Data):
    small = big = Data[0] # Asumming data is non empty 
    for i in Data: # for i in Data (alternative soln)
        #1 being the fist element, len(Data) being the  last number of iteration
        if i < small: # compares the data wherether it is smaller than the number
            small = i#if its smaller than the number, save
        elif i > big: # compares the data whether it is larger than the number
            big = i# if its larger save the data
    
    # prints the statement
    return (small, big) # return the smallest and largest number as tuple

#testing the function(test codes pls tidy up)
hi = 2, 3, 4, 5, 6, 7, 8, 9, 10,99939,1323,23849283 # some tuple number
Nice=minmax(hi) #running the fuction and assigning the result to a variable
print(Nice) #printing the tuple
print("tuple length is " + str(len(Nice))) # print the length of tuple

#solution is accepted   