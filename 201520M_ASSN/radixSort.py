#Radix sort sorting for the cost of package
# Name:Eden Will Sng Jin Xuan, Adm:201520M , Tutorial-Grp:IT2553-02

from records import*
from operator import attrgetter
import random
import names
from tabulate import tabulate
# Python program for implementation of Radix Sort
# A function to do counting sort of arr[] according to
# the digit represented by exp.

#referenced source code used: https://www.geeksforgeeks.org/radix-sort/
#referenced paper used: https://en.wikipedia.org/wiki/Radix_sort 
#youtube video referenced: https://www.youtube.com/watch?v=XiuSW_mEn7g 


def countingSort(arr, exp1):

    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i].get_cost()) // exp1
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i].get_cost()) // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
    return arr

# Method to do Radix Sort
def radixSort(arr):

    # Find the maximum number to know number of digits
    max1 = max(arr, key=lambda x: x.get_cost()) # / 
    #print(max1.get_cost()) # / 

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i #in short this helps to iterate each number in the array, for e.g. 3540, will need abt 4 passe of counting sort
    # where i is current digit number
    exp = 1
    while max1.get_cost() / exp > 1: # / 
        countingSort(arr, exp) # / 
        exp *= 10 # 
    


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


#     radixSort(theRecords)
#     print(theRecords)
#     display(theRecords)


# main()

#source: https://www.geeksforgeeks.org/radix-sort/ 
