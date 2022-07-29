# Counting sort for customer package price
# Name:Eden Will Sng Jin Xuan, Adm:201520M , Tutorial-Grp:IT2553-02
import random
import names
from tabulate import tabulate
from records import *
#source code used:
#https://www.geeksforgeeks.org/counting-sort
#youtube video ref: https://youtu.be/7zuGmKfUt7s 

def countingSort(arr):
    max_element = max(arr, key=lambda x: x.get_cost()).get_cost()
    min_element = min(arr, key=lambda x: x.get_cost()).get_cost()
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual
    # elements and initialize count array as 0
    count_arr = [0 for _ in range(range_of_elements)] # initialize count array from the range, withe every element being 0
    output_arr = [0 for _ in range(len(arr))] #the expected output array to store the list

    # Store count of each character
    for i in range(0, len(arr)):
        count_arr[arr[i].get_cost()-min_element] += 1 #get the number of times the count appears

    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_arr)): #iterate through the count array, now contains the actual position
        count_arr[i] += count_arr[i-1]

    # Build the output character array
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i].get_cost() - min_element] - 1] = arr[i] #now places the output arrays
        count_arr[arr[i].get_cost() - min_element] -= 1

    # Copy the output array to arr, so that arr now
    # contains sorted characters 
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]

    return arr


# def display(theRecords):
#     table=[]
#     for i in range(len(theRecords)):
#         table.append([i+1,theRecords[i].get_package(), theRecords[i].get_customer(), theRecords[i].get_pax(), theRecords[i].get_cost()])
#     print(" ")
#     print(tabulate(table, headers=["Row", "Package", "Customer", "Pax", "Cost"]))

# #test code for radix sort
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


#     theRecords = countingSort(theRecords)
#     print(theRecords)
#     display(theRecords)

# main()