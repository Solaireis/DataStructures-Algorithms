from regex import P
# you could make a last occurence for this practical

def firstbinarySearch( theValues, target ):
    # Start with the entire sequence of elements 
    low = 0
    high = len( theValues ) - 1 #index starts from 0 high points at -1 
    # Repeatedly subdivide the sequence in half 
    # # until the target is found
    while low <= high:
        #print("low",low)
        #print("high",high)
        # Find the midpoint of the sequence
        mid = (low + high) // 2 # In the actual binary table, middle number is always lower
        #print('mid',mid)
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
        elif theValues[mid] > target:
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
        #print("low",low)
        #print("high",high)
        # Find the midpoint of the sequence
        mid = (low + high) // 2 # In the actual binary table, middle number is always lower
        # Does the midpoint contain the target?
        # If yes, return midpoint (i.e. index of the list) 
        #try:
        if theValues[mid] == target:
            last_occurence = mid
            cont = True
            while last_occurence < (len(theValues)-1) and cont:
                if last_occurence == (len(theValues)-2): #if last_occurence is the last number in the list
                    return last_occurence
                if theValues[last_occurence+1] == target:
                    last_occurence += 1
                else:
                    cont = False
            return last_occurence 
        # Or is the target before the midpoint? 
        elif theValues[mid] > target:
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

def allBinarySearches( theValues,Target):
    first_occurence = firstbinarySearch(theValues,Target)
    last_occurence = lastbinarySearch(theValues,Target)
    theValues = []
    for i in range(first_occurence,last_occurence+1):
        theValues.append(i)
    return theValues

list = [10,18,18,18,18,23,25,34,36,42,63,74,87,92,99]
list.reverse()
print(list,len(list))
print(firstbinarySearch(list,18))
print(lastbinarySearch(list,18))
print(allBinarySearches(list,18))
print(allBinarySearches(list,99))
#Print all occurances of


