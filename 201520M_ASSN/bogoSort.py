# Bogo sort , sorts the customer names 
# Name:Eden Will Sng Jin Xuan, Adm:201520M , Tutorial-Grp:IT2553-02
import random
from records import *
import random
import names
from tabulate import tabulate

# Sorts array a[0..n-1] using Bogo sort
def bogoSort(arr): #this calls bogosort
    #n = len(arr) 
    while (is_sorted(arr)== False):
        shuffle(arr)

# To check if array is sorted or not
def is_sorted(arr):
    n = len(arr)
    for i in range(0, n-1):
        if (arr[i].get_customer().upper() > arr[i+1].get_customer().upper() ): #checks if the character value of the customer name is > than the next customer (meaning to say it isnt sorted)
            return False #return that its not sorted
    return True

# To generate permutation of the array in a random fashion, the thing about bogosort is that it hopes the random shuffling will deliver the outcome
def shuffle(arr):
    n = len(arr)
    for i in range (0,n):
        r = random.randint(0,n-1) #for every element in the array it will be shuffled randomly
        arr[i], arr[r] = arr[r], arr[i]


# test codes
# def display(theRecords):
#     table=[]
#     for i in range(len(theRecords)):
#         table.append([i+1,theRecords[i].get_package(), theRecords[i].get_customer(), theRecords[i].get_pax(), theRecords[i].get_cost()])
#     print(" ")
#     print(tabulate(table, headers=["Row", "Package", "Customer", "Pax", "Cost"]))

# # #test code for bogo sort
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


#     bogoSort(theRecords)
#     print(theRecords)
#     display(theRecords)


# main()