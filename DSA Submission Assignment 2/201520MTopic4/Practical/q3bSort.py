def last_element(a):
    return 2 #a[-1] #like never put a key at all
    #return a[-1] #key for comparisons

number = [(1,7),(1,3),(3,4,5),(2,2)]
print(number)   
listSorted = sorted(number, key=last_element)
print(listSorted)