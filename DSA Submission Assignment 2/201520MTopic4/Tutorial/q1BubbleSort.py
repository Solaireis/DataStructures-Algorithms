# Sorts a sequence in ascending order using the # optimized bubble sort algorithm
def bubbleSort_optimized( theSeq ):
    n = len( theSeq )
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1, 0, -1):
        # Set boolean variable to check occurrence of swapping
        # in inner loop
        swapped = True
        #noswap = True
        # Bubble the largest item to the end
        for j in range(i):
            if theSeq[j] > theSeq[j + 1]:
                    # Swap the j and j+1 items
                    tmp = theSeq[j]
                    theSeq[j] = theSeq[j + 1]
                    theSeq[j + 1] = tmp
    
            # Set boolean variable value if swapping occurred
            swapped = False
            #if noswap = False
        # Exit the loop if no swapping occurred
        # in the previous pass
        print("Pass ", theSeq)
        if swapped:
            break
        #if noswap:
            #break

    return theSeq

#testcode
list_of_numbers = [5,3,2,1,4]
test = [30,7,9,24,77,29] #[19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
print(" ")
print('Bubble Sort')
print(bubbleSort_optimized(list_of_numbers))
print(bubbleSort_optimized(test))

#1b.
#standard bubble sort 4 passes are required
#optimised , bubble sort 2 passes are required
# 1c. 
# if sorted already 1 pass is required
# the adv is that bubble sort has over sorting algo
# is having an efficient way to check if a list of number 
# is already sorted in order

#in test qn, first be careful of the 
# algorithm they are asking for
#they may ask for descending order or ascending order
# as long as one
# line is wrong all the line is wrong,
# u get fullmarks or zero
#do both decending and ascending order


#3a True 
#3b True
#3c True
#3d false (you dont compare the entire thing )