# bubble sort , sorts the customer names 
# Name:Eden Will Sng Jin Xuan, Adm:201520M , Tutorial-Grp:IT2553-02
from records import *
def bubbleSort(theRecords):
    #bubble sort the records.
    n = len(theRecords)
    for i in range(n - 1, 0, -1):
        # Set boolean variable to check occurrence of swapping
        # in inner loop
        swapped = True
        # Bubble the largest item to the end
        for j in range(i):
            if theRecords[j].get_customer() > theRecords[j + 1].get_customer():
                    # Swap the j and j+1 items
                    tmp = theRecords[j]
                    theRecords[j] = theRecords[j + 1]
                    theRecords[j + 1] = tmp
    
            # Set boolean variable value if swapping occurred
            swapped = False
        # Exit the loop if no swapping occurred
        # in the previous pass
        #print("Pass ", [i])
        if swapped:
            break
    
    print("")
    print("Bubble Sort:")
    return theRecords

