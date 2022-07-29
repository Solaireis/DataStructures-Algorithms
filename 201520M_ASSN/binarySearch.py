#binary search 
#201520m Eden Will Sng Jin Xuan Tutorial-Grp:IT2553-02
from turtle import up
from records import *
import random
import names
from tabulate import tabulate


def display(theRecords):
    table=[]
    for i in range(len(theRecords)):
        table.append([i+1,theRecords[i].get_package(), theRecords[i].get_customer(), theRecords[i].get_pax(), theRecords[i].get_cost()])
    print(" ")
    print(tabulate(table, headers=["Row", "Package", "Customer", "Pax", "Cost"]))

def chooseChoice(msg):
    while True:
        try:
            choice = int(input(msg))
            if choice >= 0 :
                return choice
            else:
                raise ValueError
        except ValueError:
            print("Not an Positive Integer! Please try again.")
            continue

def binarySearch(theRecords,search):
    first = firstOccurenceSearch(theRecords,search)
    last = lastOccurenceSearch(theRecords,search)
    # print(first,last)
    searchRes = []
    if first != None or last != None:
        print("records found", search)
        for i in range(first, last+1):
            searchRes.append([i+1,theRecords[i].get_package(), theRecords[i].get_customer(), theRecords[i].get_pax(), theRecords[i].get_cost()])
        print(tabulate(searchRes, headers=["Row", "Package", "Customer", "Pax", "Cost"]))
    
        theRecords = editRecords(theRecords,first,last)
        return theRecords

    else:
        print(" ")
        print("No record founds")
        print(" ")
        return -1

def firstOccurenceSearch(theRecords,search):
    #sort the records by package
    theRecords.sort(key=lambda x: x.get_package())
    display(theRecords)
    #ask the user to input the package name to search for
    result = []
    #if the package name is found, print the record
    #if the package name is not found, print "No record found"
    low = 0
    high = len(theRecords) - 1
    while low <= high:
        #print("low,high", low, high)
        mid = (low + high) // 2
        if theRecords[mid].get_package().upper() == search:
            first_occurence = mid
            cont = True
            while first_occurence > 0 and cont:
                if theRecords[first_occurence-1].get_package().upper() == search:
                    first_occurence -= 1
                else:
                    cont = False
            return first_occurence

        elif theRecords[mid].get_package().upper() < search:
            low = mid + 1
        else:
            high = mid - 1
    if not result:
        #print("No record found")
        print(" ")
    else:
        print("Found record(s):")
        for i in range(len(result)):
            displayRecord(i, result)

def lastOccurenceSearch(theRecords,search):
    #sort the records by package
    theRecords.sort(key=lambda x: x.get_package())
    display(theRecords)
    #ask the user to input the package name to search for
    result = []
    #if the package name is found, print the record
    #if the package name is not found, print "No record found"
    low = 0
    high = len(theRecords) - 1
    while low <= high:
        #print("low,high", low,high)
        mid = (low + high) // 2
        if theRecords[mid].get_package().upper() == search:
            last_occurence = mid
            cont = True
            while  last_occurence < 10 and cont:
                if last_occurence == 9:
                    return last_occurence
                if theRecords[last_occurence+1].get_package().upper() == search:
                    last_occurence += 1
                else:
                    cont = False
            return last_occurence 

        elif theRecords[mid].get_package().upper() < search:
            low = mid + 1
        else:
            high = mid - 1
    if not result:
        #print("No record found")
        print(" ")

def editRecords(results,first,last):
    update = input("Do you want to update the records? (Y/N)")
    while True:
        if update.upper() == "Y":
            choice = chooseChoice("Select the records you want to update: ")
            if choice > first and choice <= last:
                choice -= 1
                i = choice
                while True:
                    print("Which field do you want to update?")
                    print("1. Package")
                    print("2. Number of pax")
                    print("3. Cost per pax")
                    print("0. to End Query")
                    upd_field= chooseChoice("Enter the field you'll like to update: ")
                    if upd_field==1:
                        upd_package=input("Enter the new package: ")
                        results[i].set_package(upd_package)
                    elif upd_field==2:
                        upd_pax=chooseChoice("Enter the new number of pax: ")
                        results[i].set_pax(upd_pax)
                    elif upd_field==3:
                        upd_cost=chooseChoice("Enter the new cost per pax: ")
                        results[i].set_cost(upd_cost)
                    elif upd_field==0:
                        break
                    else:
                        print("Invalid input")
                        continue
                    if upd_field == 1 or upd_field == 2 or upd_field == 3 or upd_field == 4:
                        searchRes1 = []
                        searchRes1.append([choice+1, results[choice].get_package(), results[choice].get_customer(), results[choice].get_pax(), results[choice].get_cost()])
                        print(" ")
                        print(tabulate(searchRes1, headers=["Row", "Package", "Customer", "Pax", "Cost"]))
                    return results
            else:
                print("Invalid input")
                continue

        elif update.upper() == "N":
            return results
        else:
            print("Please put either Y or N")
            continue


# #test cases for binary search
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

#     print(binarySearch(theRecords,"KING"))
#     print(binarySearch(theRecords,"QUEEN"))
#     print(binarySearch(theRecords,"DOUBLE"))
#     print(binarySearch(theRecords,"TWIN"))


# main()

#if user inputs any number which arent in the range youll have to error handle it / 

