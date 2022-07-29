# selection sort by package name 
# Name:Eden Will Sng Jin Xuan, Adm:201520M , Tutorial-Grp:IT2553-02

from records import *
def selectionSort(theRecords):
    #selection sort the records.
    n = len(theRecords)
    for i in range(n - 1):
        minIndex = i
        for j in range(i + 1, n):
            if theRecords[j].get_package() < theRecords[minIndex].get_package():
                minIndex = j
        # Swap the i and minIndex items
        tmp = theRecords[i]
        theRecords[i] = theRecords[minIndex]
        theRecords[minIndex] = tmp

    print("")
    print("Selection Sort:")
    return theRecords
        
