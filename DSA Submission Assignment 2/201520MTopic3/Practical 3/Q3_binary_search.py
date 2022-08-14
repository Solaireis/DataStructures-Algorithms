from regex import P
# you could make a last occurence for this practical

def firstbinarySearch( theValues, target ):
    # Start with the entire sequence of elements 
    low = 0
    high = len( theValues ) - 1 #index starts from 0 high points at -1 
    # Repeatedly subdivide the sequence in half 
    # # until the target is found
    while low <= high:
        print("low",low)
        print("high",high)
        # Find the midpoint of the sequence
        mid = (low + high) // 2 # In the actual binary table, middle number is always lower
        print('mid',mid)
        # Does the midpoint contain the target?
        # If yes, return midpoint (i.e. index of the list) 
        #try:
        if theValues[mid] == target:
            first_occurence = mid
            cont = True
            while first_occurence > 0 and cont:
                if theValues[first_occurence-1] == target:
                    first_occurence -= 1
                else:
                    cont = False
            return first_occurence
        # Or is the target before the midpoint? 
        elif theValues[mid] < target:
            low = mid + 1
        # Or is the target after the midpoint?
        else: 
            high = mid - 1

        # except IndexError:
        #     print("number doesnt exist")
        #     return -1

        
    # If the sequence cannot be subdivided further, 
    # target is not in the list of values
    return -1

def lastbinarySearch( theValues, target ):
    # Start with the entire sequence of elements 
    low = 0
    high = len( theValues ) - 1 #index starts from 0 high points at -1 
    # Repeatedly subdivide the sequence in half 
    # # until the target is found
    while low <= high:
        print("low",low)
        print("high",high)
        # Find the midpoint of the sequence
        mid = (low + high) // 2 # In the actual binary table, middle number is always lower
        # Does the midpoint contain the target?
        # If yes, return midpoint (i.e. index of the list) 
        #try:
        if theValues[mid] == target:
            first_occurence = mid
            cont = True
            while theValues[first_occurence] == target and cont:
                if theValues[first_occurence+1] == target:
                    first_occurence += 1
                else:
                    cont = False
            return first_occurence 
        # Or is the target before the midpoint? 
        elif theValues[mid] < target:
            low = mid + 1
        # Or is the target after the midpoint?
        else: 
            high = mid - 1

        # except IndexError:
        #     print("number doesnt exist")
        #     return -1

        
    # If the sequence cannot be subdivided further, 
    # target is not in the list of values
    return -1

# testcode= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
# testcode2= [1,1,3,4,4,5,7,7,7,8,8,9,9,10]
# print("the index found was", binarySearch(testcode, 22))
# print("the index found was", binarySearch(testcode2, 8))
# print("the index found was", binarySearch(testcode2, 7))
# print("the index found was", binarySearch(testcode2, 1))
# print("the index found was", binarySearch(testcode2, 9))
# print("the index found was", binarySearch(testcode2, 6))
# print("the index found was", binarySearch(testcode2, 22))
# testcode3 = [1,2,3]
# testcode4=[10,23,25,34,36,36,42,42,42,42,42,63,74,87,92,99]
# print(testcode4[firstbinarySearch(testcode4,42)],firstbinarySearch(testcode4,42))
# print(testcode4[lastbinarySearch(testcode4,42)],lastbinarySearch(testcode4,42))

# print(testcode4[firstbinarySearch(testcode4,36)],firstbinarySearch(testcode4,36))
# print(testcode4[lastbinarySearch(testcode4,36)],lastbinarySearch(testcode4,36))

list = [10,23,25,34,36,42,63,74,87,92,99]
print(firstbinarySearch(list,18))