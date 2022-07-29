# Name:Eden Will Sng Jin Xuan, Adm:201520M , Tutorial-Grp:IT2553-02
# main python file to be runned
from records import *
from linearSearch import *
from binarySearch import *
import random
import names
from bubbleSort import *
from selectionSort import *
from insertionSort import *
from tabulate import tabulate
from radixSort import *
from stalinSort import *
from heapSort import *
from bogoSort import *
from countingSort import *
from shellSort import *

#Function that displays the UI for the user
def displayChoice():
    print("----------------------------------------------------------------")
    print("Welcome to Eden Staycation booking records system")
    print("Choose the options below:")
    print("1. Display records")
    print("2. Bubble Sort | Customer Name")
    print("3. Selection Sort | Package Name")
    print("4. Insertion Sort | Package Cost")
    print("5. Linear Search | Customer Name")
    print("6. Binary Search | Package Name")
    print("7. List records | Package Costs")
    print("8. Advanced Algo")
    print("9. Joker Algo")
    print("0. Exit the system")
    print("----------------------------------------------------------------")
    print(" ")

#Validation for integer inputs by the user
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

#tabulate function to easily deploy the table
def displayTable(table):
    print(tabulate(table, headers=["Row", "Package", "Customer", "Pax", "Cost"]))

def main():
    # room types allowed ["Single", "Double", "Triple", "Quad", "Queen", "King", "Twin", "Double-Double", "Double-Twin"]
    package = ["Single", "Double", "Triple", "Quad", "Queen", "King", "Twin", "Double-Double", "Double-Twin"] 
    theRecords = [] #the record is left blank so it can be initialize
    for i in range(8): # 8 random records are generated
        thePackage = random.choice(package)
        theCust = names.get_first_name()
        thePax = random.randint(1,10)
        theCost = random.randint(100,5000)
        i = Record(thePackage, theCust, thePax, theCost)
        theRecords.append(i)
    for i in range(2): # 2 random records with customer name: Eden
        thePackage = random.choice(package)
        theCust = "Eden"
        thePax = random.randint(1,10)
        theCost = random.randint(100,5000)
        i = Record(thePackage, theCust, thePax, theCost)
        theRecords.append(i)

    while True: #assumes this hotel runs infinitely until user wants to exit()
        displayChoice() #calls the display function
        choice = chooseChoice("Input your choice: ") #calls the choose function
        sortedTable = [] #this is for the sorting algorithms to place the records for displaying (this will be deleted and override)
        table = [] #this is for the first table to be displayed to the user

        #Display records to user
        if choice == 1:
            for i in range(len(theRecords)):
                table.append([i+1,theRecords[i].get_package(), theRecords[i].get_customer(), theRecords[i].get_pax(), theRecords[i].get_cost()])
            print(" ")
            displayTable(table)
            print(" ")
            r = input("Choose any to return: ")
            continue

        #Bubble Sort Function
        elif choice == 2:
            sorted = bubbleSort(theRecords)
            for i in range(len(sorted)):
                sortedTable.append([i+1,sorted[i].get_package(), sorted[i].get_customer(), sorted[i].get_pax(), sorted[i].get_cost()])
            displayTable(sortedTable)
            print(" ")
            r = input("Choose any to return: ")
            continue

        #Selection Sort Function
        elif choice == 3:
            sorted = selectionSort(theRecords)
            for i in range(len(sorted)):
                sortedTable.append([i+1,sorted[i].get_package(), sorted[i].get_customer(), sorted[i].get_pax(), sorted[i].get_cost()])
            displayTable(sortedTable)
            print(" ")
            r = input("Choose any to return: ")
            continue

        #Insertion Sort Function
        elif choice == 4:
            sorted = insertionSort(theRecords)
            for i in range(len(sorted)):
                sortedTable.append([i+1,sorted[i].get_package(), sorted[i].get_customer(), sorted[i].get_pax(), sorted[i].get_cost()])
            displayTable(sortedTable)
            print(" ")
            r = input("Choose any to return: ")
            continue
        
        #Linear Search Function
        elif choice == 5:
            #display the table
            for i in range(len(theRecords)):
                table.append([i+1,theRecords[i].get_package(), theRecords[i].get_customer(), theRecords[i].get_pax(), theRecords[i].get_cost()])
            displayTable(table)
            print(" ")
            
            search = str(input("Enter the customer name to search for: "))
            results = linearSearch(theRecords,search.upper())
            if results == -1:
                r = input("Choose any to return: ")
                continue
            else:
                theRecords = results
                for i in range(len(results)):
                    sortedTable.append([i+1,results[i].get_package(), results[i].get_customer(), results[i].get_pax(), results[i].get_cost()])
                displayTable(sortedTable)
                r = input("Choose any to return: ")
                continue
        
        #Binary Search Function
        elif choice == 6:
            #display the table
            for i in range(len(theRecords)):
                table.append([i+1,theRecords[i].get_package(), theRecords[i].get_customer(), theRecords[i].get_pax(), theRecords[i].get_cost()])
            displayTable(table)
            print(" ")

            search = str(input("Enter the package name to search for: "))
            results = binarySearch(theRecords,search.upper())
            if results == -1:
                r = input("Choose any to return: ")
                continue
            else:
                theRecords = results
                print(" ")
                for i in range(len(theRecords)):
                    sortedTable.append([i+1,theRecords[i].get_package(), theRecords[i].get_customer(), theRecords[i].get_pax(), theRecords[i].get_cost()])
                displayTable(sortedTable)
                print(" ")
                r = input("Choose any to return: ")

        #List the records by a user specified range
        elif choice == 7:
            radixSort(theRecords) # uses the radix sort function to sort them nicely by package cost
            for i in range(len(theRecords)):
                table.append([i+1,theRecords[i].get_package(), theRecords[i].get_customer(), theRecords[i].get_pax(), theRecords[i].get_cost()])
            print(" ")
            displayTable(table)
            print(" ")
            rowCount = [] #counter for the if else statement
            while True:
                lowRange = chooseChoice("Choose Lower Price Range: ")
                if lowRange > 0:
                    break
                else:
                    print("Integer cannot be negative Try again.")

            while True:
                highRange = chooseChoice("Choose Upper Price Range: ")
                if highRange > 0 and highRange <= 5000:
                    break

                else:
                    print("Invalid Range, the maximum range is 5000! Try again.")
                    continue
            
            if lowRange < highRange:
                for i in range(len(theRecords)):
                    if lowRange <= theRecords[i].get_cost() <= highRange:
                        sortedTable.append([i+1,theRecords[i].get_package(), theRecords[i].get_customer(), theRecords[i].get_pax(), theRecords[i].get_cost()])
                        rowCount.append(i)

                displayTable(sortedTable)
            else:
                for i in range(len(theRecords)):
                    if highRange <= theRecords[i].get_cost() <= lowRange:
                        sortedTable.append([i+1,theRecords[i].get_package(), theRecords[i].get_customer(), theRecords[i].get_pax(), theRecords[i].get_cost()])
                        rowCount.append(i)
                displayTable(sortedTable)
                
            print(rowCount)
            

            while True:
                choice = input("Do you want to update the records Y/N: ")
                if choice.upper() == "Y":
                    while True:
                        rowChoice = chooseChoice("Choose the row to update: ")
                        if rowChoice >= min(rowCount) and rowChoice <= (max(rowCount)+1):
                            break
                        else:
                            print("Invalid Row! Try again.")
                            continue

                    while True:
                        rowChoice -= 1
                        print("Which field do you want to update?")
                        print("1. Package")
                        print("2. Number of pax")
                        print("3. Cost per pax")
                        print("0. to End Query")
                        upd_field= chooseChoice("Enter the field you'll like to update: ")
                        if upd_field==1:
                            upd_package=input("Enter the new package: ")
                            theRecords[rowChoice].set_package(upd_package)
                        elif upd_field==2:
                            upd_pax=chooseChoice("Enter the new number of pax: ")
                            theRecords[rowChoice].set_pax(upd_pax)
                        elif upd_field==3:
                            upd_cost=chooseChoice("Enter the new cost per pax: ")
                            theRecords[rowChoice].set_cost(upd_cost)
                        elif upd_field==0:
                            break
                        else:
                            print("Invalid input")
                            continue
                        if upd_field == 1 or upd_field == 2 or upd_field == 3 or upd_field == 4:
                            searchRes1 = []
                            searchRes1.append([rowChoice+1, theRecords[rowChoice].get_package(), theRecords[rowChoice].get_customer(), theRecords[rowChoice].get_pax(), theRecords[rowChoice].get_cost()])
                            print(" ")
                            print(tabulate(searchRes1, headers=["Row", "Package", "Customer", "Pax", "Cost"]))

                        sortedTable = [] #resets the tabulate table 
                        for i in range(len(theRecords)):
                            if lowRange <= theRecords[i].get_cost() <= highRange:
                                sortedTable.append([i+1,theRecords[i].get_package(), theRecords[i].get_customer(), theRecords[i].get_pax(), theRecords[i].get_cost()])
                        displayTable(sortedTable)
                        break
                    break

                    # update the records next

                elif choice.upper() == "N":
                    break
                else:
                    print("Invalid Input! Try again.")
                    continue
            #print("Thank you for using Eden Staycation to book with our hotel service")

            r = input("Choose any to return: ")
            #put validation to factor in if user put beyond the range 
            continue
        
        #Extra Algos used for the project
        elif choice == 8: 
            while True:
                print("Welcome to The Extra Algos ")
                print("Choose the options below:")
                print("1. Radix Sort | Package Cost")
                print("2. Heap Sort | Customer Name")
                print("3. Counting Sort | Package Cost")
                print("4. Shell Sort | Package Cost")
                print("0. to exit Advanced Algos")
                print("----------------------------------------------------------------")
                print(" ")
                choice = chooseChoice("Input your choice: ")

                # Radix Sort Fn
                if choice == 1:
                    sortedTable = []
                    print(" ")
                    print(" -- Radix Sort | Package Cost --")
                    print(" ")
                    radixSort(theRecords)
                    for i in range(len(theRecords)):
                        sortedTable.append([i+1,theRecords[i].get_package(), theRecords[i].get_customer(), theRecords[i].get_pax(), theRecords[i].get_cost()])
                    displayTable(sortedTable)
                    print(" ")
                    r = input("Choose any to return: ")
                    continue
                
                # Heap Sort Fn
                if choice == 2:
                    sortedTable = []
                    print(" ")
                    print(" -- Heap Sort | Customer Name --")
                    print(" ")
                    heapSort(theRecords)
                    for i in range(len(theRecords)):
                        sortedTable.append([i+1,theRecords[i].get_package(), theRecords[i].get_customer(), theRecords[i].get_pax(), theRecords[i].get_cost()])
                    displayTable(sortedTable)
                    print(" ")
                    r = input("Choose any to return: ")
                    continue
                
                # Counting Sort Fn
                if choice == 3:
                    sortedTable = []
                    print(" ")
                    print(" -- Counting Sort | Package Cost --")
                    print(" ")
                    theRecords = countingSort(theRecords)
                    for i in range(len(theRecords)):
                        sortedTable.append([i+1,theRecords[i].get_package(), theRecords[i].get_customer(), theRecords[i].get_pax(), theRecords[i].get_cost()])
                    displayTable(sortedTable)
                    print(" ")
                    r = input("Choose any to return: ")
                    continue
                
                if choice == 4:
                    sortedTable = []
                    print(" ")
                    print(" -- Shell Sort | Package Cost --")
                    print(" ")
                    shellSort(theRecords)
                    for i in range(len(theRecords)):
                        sortedTable.append([i+1,theRecords[i].get_package(), theRecords[i].get_customer(), theRecords[i].get_pax(), theRecords[i].get_cost()])
                    displayTable(sortedTable)
                    print(" ")
                    r = input("Choose any to return: ")
                    continue
                
                if choice == 0:
                    break

        #Inefficient algos used for the project
        elif choice == 9:
            while True:
                print("Welcome to The Joker Algos ")
                print("Choose the options below:")
                print("1. StalinSort | Customer")
                print("2. bogoSort | Customer")
                print("----------------------------------------------------------------")
                print(" ")
                choice = chooseChoice("Input your choice: ")

                # StalinSort Fn
                if choice == 1:
                    print(" ")
                    print(" -- StalinSort ☭ | Customer --")
                    print(" ")
                    stalinSort(theRecords)
                    for i in range(len(theRecords)):
                        sortedTable.append([i+1,theRecords[i].get_package(), theRecords[i].get_customer(), theRecords[i].get_pax(), theRecords[i].get_cost()])
                    displayTable(sortedTable)
                    print(" ")
                    r = input("Choose any to return: ")
                    break
                
                # bogoSort Fn
                if choice == 2:
                    print(" ")
                    print(" -- bogoSort ☭ | Customer --")
                    print(" ")
                    bogoSort(theRecords)
                    for i in range(len(theRecords)):
                        sortedTable.append([i+1,theRecords[i].get_package(), theRecords[i].get_customer(), theRecords[i].get_pax(), theRecords[i].get_cost()])
                    displayTable(sortedTable)
                    print(" ")
                    r = input("Choose any to return: ")
                    break
                    
        #Exit the program
        elif choice == 0:
            print("Thank you for using Eden Staycation to book with our hotel service")
            break
        
        #if user didnt enter the right number
        else:
            print("Please enter the correct number")
            continue

#runs the program
if __name__ == "__main__":

    main()