# An iterative implementation of Binary Search
def binarySearch( theValues, target ):
    # Start with the entire sequence of elements low = 0
    high = len( theValues ) - 1
    low = 0
    # Repeatedly subdivide the sequence in half # until the target is found
    while low <= high:
            # Find the midpoint of the sequence
        mid = (high + low) // 2
        # Does the midpoint contain the target?
        # If yes, return midpoint (i.e. index of the list)
        if theValues[mid] == target:
            return mid
        #Or is the target before the midpoint? 
        elif target < theValues[mid]:
            high = mid - 1
        # Or is the target after the midpoint? 
        else:
            low = mid + 1
    # If the sequence cannot be subdivided further, 
    # target is not in the list of values
    return -1

# A recursive implementation of Binary Search
def recBinarySearch( target, theValues, first, last ):
    # If the sequence of values cannot be subdivided further,
    # we are done
    if first > last: # BASE CASE #1
        return False
    else:
    # Find the midpoint of the sequence 
        mid = (first + last) // 2
    # Does the element at the midpoint contain the target?
    if theValues[mid] == target:
        return True # BASE CASE #2
    # or does the target precede the element at the midpoint?
    elif target < theValues[mid]: 
        return recBinarySearch( target, theValues, first, mid - 1 )
    # or does the target follows the element at the midpoint?
    else:
        return recBinarySearch( target, theValues, mid + 1, last )

#testcode
theValues = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(binarySearch( theValues,11))
print(recBinarySearch( 5, theValues, 0, len(theValues) - 1 ))