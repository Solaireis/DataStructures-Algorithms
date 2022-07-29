#Shell sort sorting for sorting names of package
# Name:Eden Will Sng Jin Xuan, Adm:201520M , Tutorial-Grp:IT2553-02
from records import *

import random
import names
from tabulate import tabulate 

#Sources used:
#source code: https://www.geeksforgeeks.org/shellsort/
#Video materials to help better learn this sorting algorithms
# 1) https://youtu.be/SHcPqUe2GZM
# 2) https://youtu.be/g06hNBhoS1k

def shellSort(arr):
    # code here
    n = len(arr)
    gap=n//2

    while gap>0:
        j=gap
        # Check the array in from left to right
        # Till the last possible index of j
        while j<n:
            i=j-gap # This will keep help in maintain gap value
            
            while i>=0:
                # If value on right side is already greater than left side value
                # We don't do swap else we swap
                if arr[i+gap].get_package() >arr[i].get_package():

                    break
                else:
                    arr[i+gap],arr[i]=arr[i],arr[i+gap]

                i=i-gap # To check left side also
                            # If the element present is greater than current element
            j+=1
        gap=gap//2


# def display(theRecords):
#     table=[]
#     for i in range(len(theRecords)):
#         table.append([i+1,theRecords[i].get_package(), theRecords[i].get_customer(), theRecords[i].get_pax(), theRecords[i].get_cost()])
#     print(" ")
#     print(tabulate(table, headers=["Row", "Package", "Customer", "Pax", "Cost"]))

# # #test code for radix sort
# def main():
#     package = ["Single", "Double", "Triple", "Quad", "Queen", "King", "Twin", "Double-Double", "Double-Twin"] 
#     theRecords = []
#     for i in range(10):
#         thePackage = random.choice(package)
#         theCust = names.get_first_name()
#         thePax = random.randint(1,10)
#         theCost = random.randint(100,5000)
#         i = Record(thePackage, theCust, thePax, theCost)
#         theRecords.append(i)


#     shellSort(theRecords)
#     print(theRecords)
#     display(theRecords)

# main()

