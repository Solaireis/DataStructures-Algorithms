# Sort a sequence in ascending order using the selection sort # algorithm
def selectionSort( theSeq , choice):
    n = len( theSeq )

    if choice == "A":
        for i in range(n - 1):
            # Assume the ith element is the smallest.
            smallNdx = i
            # Determine if any other element contains a smaller value. 
            for j in range(i+1, n):
                if theSeq[j] < theSeq[smallNdx]: smallNdx = j
            # Swap the ith value and smallNdx value only if the
            # smallest value is not already in its proper position. 
            if smallNdx != i:
                tmp = theSeq[i]
                theSeq[i] = theSeq[smallNdx]
                theSeq[smallNdx] = tmp
                print("Pass:",i , "\t", theSeq)
    
    elif choice == "D":
        for i in range(n - 1):
            # Assume the ith element is the smallest.
            largeNdx = i
            # Determine if any other element contains a smaller value. 
            for j in range(i+1, n):
                if theSeq[j] > theSeq[largeNdx]: largeNdx = j
            # Swap the ith value and smallNdx value only if the
            # smallest value is not already in its proper position. 
            if largeNdx != i:
                tmp = theSeq[i]
                theSeq[i] = theSeq[largeNdx]
                theSeq[largeNdx] = tmp
                print("Pass:",i , "\t", theSeq)
                
# Test codes
list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
list_of_numbers2 = [12,7,9,24,7,29,5,3,11,7]

print(" ")
print("Sorting in Ascending order:")
print('Input List:', list_of_numbers) 
selectionSort(list_of_numbers, "A") 
print('Sorted List:', list_of_numbers)

print(" ")
print("Sorting in decending order:")
print('Input List:', list_of_numbers)
selectionSort(list_of_numbers, "D")
print('Sorted List:', list_of_numbers)

selectionSort(list_of_numbers2, "D")
print(list_of_numbers2)
#answer
# for i in range(i+1, n):
    #if choice == "A":
        #if theSeq[j] < theSeq[smallNdx]:
            #smallNdx = j
    #elif choice == "D":
        #if theSeq[j] > theSeq[largeNdx]:
            #largeNdx = j

#compare the sorting method based on efficiency