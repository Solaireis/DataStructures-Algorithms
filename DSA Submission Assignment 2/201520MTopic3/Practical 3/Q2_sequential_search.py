def sequentialSearch( theValues, target ): 
    n = len( theValues )

    for i in range(n):
        # If the target is in the ith element, return True
        print(i) 
        if theValues[i] == target:
            return True

    return False # If not found, return False

def sortedSequentialSearch( theValues, target ):
    n = len( theValues )
    for i in range(n):
        # If the target is in the ith element, return True 
        print(i)
        if theValues[i] == target:
            return True
        elif theValues[i] > target: #Does not compare the reamining is number is already sorted
            return False
        
    return False # If not found, return False

testcode = [10,7,1,3,-4,2,20,99,4,5]
testcode2 = [-1,2,3,4,5,6,7,8,9]
print(sequentialSearch(testcode, 5))
print(sequentialSearch(testcode,6))
print(sortedSequentialSearch(testcode2, 5))
print(sortedSequentialSearch(testcode2, 6))