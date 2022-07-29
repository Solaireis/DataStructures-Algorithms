#insertion sort, sorts the cost of package
# Name:Eden Will Sng Jin Xuan, Adm:201520M , Tutorial-Grp:IT2553-02

from records import *
def insertionSort(theRecords):
    #insertion sort the records.
    n = len(theRecords)
    for i in range(1, n):
        key = theRecords[i]
        j = i - 1
        while j >= 0 and theRecords[j].get_cost() > key.get_cost():
            theRecords[j + 1] = theRecords[j]
            j -= 1
        theRecords[j + 1] = key
    
    print("")
    print("Insertion Sort:")
    return theRecords