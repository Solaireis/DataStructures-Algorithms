# Heap sort, sorts the customer names 
# Name:Eden Will Sng Jin Xuan, Adm:201520M , Tutorial-Grp:IT2553-02

from records import *
import random
import names
from tabulate import tabulate
# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap

#sources used in these sorting Algos
#sourcecode gathered: https://www.geeksforgeeks.org/heap-sort/
#video reference helping me
# 1) https://www.youtube.com/watch?v=2DmK_H7IdTo
# 2) https://www.youtube.com/watch?v=H5kAcmGOn4Q
# 3) https://www.youtube.com/watch?v=MtQL_ll5KhQ

# Article references: https://en.wikipedia.org/wiki/Heapsort 


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1 #left side of the child
    r = 2 * i + 2     # right = 2*i + 2 #left side of the child

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest].get_customer().upper() < arr[l].get_customer().upper():
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest].get_customer().upper() < arr[r].get_customer().upper():
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size

def heapify2(arr, n, i):
    smallest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1 #left side of the child
    r = 2 * i + 2     # right = 2*i + 2 #left side of the child

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[smallest].get_cost() > arr[l].get_cost():
        smallest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[smallest].get_cost() > arr[r].get_customer():
        smallest = r

    # Change root, if needed
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, smallest)

# The main function to sort an array of given size

def heapSort(arr):
    n = len(arr)

    # Build a maxheap acending order.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    # # Build a minheap decending order.
    # for i in range(n//2 - 1, -1, -1):
    #     heapify2(arr, n, i)

    # # One by one extract elements
    # for i in range(n-1, 0, -1):
    #     arr[i], arr[0] = arr[0], arr[i]  # swap
    #     heapify2(arr, i, 0)

def display(theRecords):
    table=[]
    for i in range(len(theRecords)):
        table.append([i+1,theRecords[i].get_package(), theRecords[i].get_customer(), theRecords[i].get_pax(), theRecords[i].get_cost()])
    print(" ")
    print(tabulate(table, headers=["Row", "Package", "Customer", "Pax", "Cost"]))

#test code for radix sort
def main():
    package = ["Single", "Double", "Triple", "Quad", "Queen", "King", "Twin", "Double-Double", "Double-Twin"] 
    theRecords = []
    for i in range(10):
        thePackage = random.choice(package)
        theCust = names.get_first_name()
        thePax = random.randint(1,10)
        theCost = random.randint(100,5000)
        i = Record(thePackage, theCust, thePax, theCost)
        theRecords.append(i)


    heapSort(theRecords)
    print(theRecords)
    display(theRecords)


main()

#[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]