def reverseInsertionSort(theSeq):
    n = len(theSeq)
    print("Pass:", "0","\t", theSeq)
    for i in range(1, n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value > theSeq[pos - 1]:
            theSeq[pos] = theSeq[pos-1]
            pos -= 1
        theSeq[pos] = value
        print("Pass:",i , "\t", theSeq)

# Test codes
list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]

print(" ")
print('Reverse Insertion Sort') 
reverseInsertionSort(list_of_numbers)