# Linear Search searches for customer names 
# Name:Eden Will Sng Jin Xuan, Adm:201520M , Tutorial-Grp:IT2553-02

from records import *
from tabulate import *

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

def linearSearch(arr, x):
    searchResults = []
    searchIndex = []
    #found = False
    for i in range(len(arr)):
        if arr[i].get_customer().upper() == x:
            searchResults.append(arr[i])
            searchIndex.append(i)
            found = True
        
        # if found == False:
        #     print("No record found")
        #     return arr

    return outputSearch(searchResults,searchIndex,arr)

def outputSearch(results,index,arr):
    if not results:
        print(" ")
        print("No record found")
        print(" ")
        return -1

    if results:
        print("Found record(s):")
        # for i in range(len(arr)):
        #     displayRecord(i,arr)
        table = []
        for i in range(len(results)):
            table.append([i+1,results[i].get_package(), results[i].get_customer(), results[i].get_pax(), results[i].get_cost()])
        
        while True:
            print(tabulate(table, headers=['No.', 'Package', 'Customer', 'Pax', 'Cost']))
            print("Which Record do you want to update?")
            upd_cust=chooseChoice("Enter Record Row: ")
            if upd_cust > 0 and upd_cust <= len(results):
                break
            else:
                print("Invalid input")
                continue
            
        for i in range(len(results)):
            if i == (upd_cust - 1):
                
                while True:
                    print("Which field do you want to update?")
                    print("1. Package")
                    print("2. Number of pax")
                    print("3. Cost per pax")
                    print("0. to End Query")
                    upd_field=chooseChoice("Enter the number: ")
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

                    print("Record updated")
                    print("Heres your changes")
                    table = []
                    for i in range(len(results)):
                        table.append([i+1,results[i].get_package(), results[i].get_customer(), results[i].get_pax(), results[i].get_cost()])
                    print(tabulate(table, headers=['No.', 'Package', 'Customer', 'Pax', 'Cost']))


        #update the results table
        for i in range(len(results)):
            arr[index[i]] = results[i]
        return arr



#add test case to make a duplicate test case
#two records which arent duplicates