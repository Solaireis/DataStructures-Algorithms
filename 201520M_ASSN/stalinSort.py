#Stalin sort, sorts the customer names 
# Name:Eden Will Sng Jin Xuan, Adm:201520M , Tutorial-Grp:IT2553-02

#source code used: https://www.geeksforgeeks.org/add-elements-in-start-to-sort-the-array-variation-of-stalin-sort/
# Github repository helping me understand stalin sort 
# https://github.com/gustavo-depaula/stalin-sort 

from records import *

    # ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⡿⡿⢿⣿⣿⣿⣿⣿⣟⣛⣿⣾⣶⣶⣶⣶⣬⣽⣛⠛⣿⣿⣿⣿⣿⣿⣿⣿
    # ⠿⠿⠿⠿⠛⠙⠻⠟⠃⠃⠓⠎⠂⠒⠁⠘⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣌⠉⠉⠉⠟⠛⠈⠁
    # ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣷⣿⣿⠿⠛⠟⢿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠄⠄⠄⠐⠄⠄
    # ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠈⢻⣿⣿⣿⣶⣶⣶⣴⠄⠄
    # ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢿⠏⢀⣤⣤⣀⣀⢀⣀⣀⣀⣀⠻⣿⣿⣿⣿⣿⣿⣿⠄⠄
    # ⠄⠄⠄⠂⠄⠄⠄⠐⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⡘⠄⠐⢚⣿⡿⠇⠈⣿⣿⣶⠿⠄⢻⣭⣿⣿⣿⡟⠉⠄⡀
    # ⣧⡀⢀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠄⠄⢀⡄⠄⠄⢠⡀⠄⠄⣠⡬⢫⣿⣿⣷⢟⣽⠄⠄
    # ⣿⣷⠸⠷⡒⠒⠚⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡒⠘⠄⣼⢋⣈⣷⣶⣎⣙⣶⣶⣿⠥⠈⠉⠉⠉⠈⠁⠄⠄
    # ⣿⣿⣶⣷⣿⣷⣶⣶⣾⣶⣷⣿⣿⣿⣿⣿⣿⣿⠿⠄⢰⣾⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠛⢋⣠⣿⣦⣿⣯⣉⣉⣉⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⣿⡿⠟⠛⠛⠉⠉⠉⠄⢀⢀⡀⡀⣨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣟⣁⣠⣰⣾⣤⣶⣵⠢⣠⣿⣿⣿⣶⣽⠿⢋⣹⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡻⢿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣏⠈⢿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⡿⠃⣠⢿⡧⠤⡄⢉⣿⣿⣿⡿⠿⠟⠇⠙⢿⣷⣿⡻⣿⣿⣿⣿
    # ⡿⢡⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⢰⣿⣿⣿⣿⣿⣷⡈⠛⢁⣤⣶⣿⡶⡁⠄⢻⣿⣿⣶⣿⣿⣿
    # ⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠄⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠄⠄⠄⠹⣿⣿⣿⣿⣯
    # ⣾⣿⣿⣿⣿⠿⠟⢛⣟⣉⡍⠉⠄⠄⢀⣼⡿⠛⠉⠉⠚⠿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠄⠁⠄⠄⠹⣿⣿⣿⣿
    # ⢿⣏⣭⣴⣶⣶⣾⣿⣿⣿⣅⣢⣤⣶⣿⣏⣀⣀⣤⣈⣄⣀⣀⣈⡿⠋⠉⠉⠉⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿
    # ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣷⣿⣿⣶⣤⣀⠄⠄⡀⠄⢸⣿⣿⣿


def stalinSort(arr): #this is the nondestructive variant of stalin sort which actually sorts the array, the original will destroy the records

    j = 0 #a counter to keep track of the number of passes in the array
    while True:
        moved = 0
        for i in range(len(arr) - 1 - j): #the len of array will -1 because of how arrays works, 
            #the -j is the number of times the array has been passed(each pass is one pass)
            
            if arr[i].get_customer().upper() > arr[i + 1].get_customer().upper(): 
                arr.insert(moved, arr.pop(i + 1))
                moved += 1
                #comparision if the customer name is greater than the next customer name, 
                #if it is the customer name will go to index 0 , and pop out of the array
                # e.g. [1,2,3,4,3,1]  at arr[3] > arr[4] , it will push arr[4] to arr[0] and pop out arr[4]
                #      Result : [3,1,2,3,4,1]
                # this is iterated many times till it is sorted
        j += 1 #counter to count number of passes, 
        if moved == 0: #once the range is finished, moved will be 0, and it will stop the while loop
            break
    return arr






    # ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣛⢻⠛⠛⡟⡛⠻⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡿⡿⠿⣿⠿⢟⠛⠿⣿⣿⣿⣿⣿⣿⣿⣟⣛⣉⣽⣿⣿⣧⣿⣷⣿⣿⣾⣶⣯⣧⣬⣭⣉⠉⢛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣾⣿⣿⣿⣿⣿⣿⠳⡿⠿⠿⠿⠇⡷⠳⠤⠘⢿⠍⡦⣀⣊⠤⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⠚⠿⣿⠻⠿⢿⢿⣿⡟⠉⠛⠉
    # ⠛⠉⠋⠋⠉⠉⠁⠄⠄⠄⠁⠁⠄⠄⠄⠄⠄⠄⠈⠄⠄⠄⠄⠄⠄⠄⠄⢰⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄⠄⠄⠄⠈⠑⠄⠄⠄⠄⠄
    # ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢾⣿⣿⣿⣿⣿⡿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠄⠄⠂⠄⠄⠄⠄⠄⠄⠄
    # ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⡿⠋⠄⠄⠄⠄⠄⠈⠙⠛⠋⠉⠉⠋⠙⢿⣿⣿⣿⣿⣿⣤⣴⣷⣄⣠⡄⡄⠄⠄⠄
    # ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⢿⣿⣿⠅⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠃⠄⠄
    # ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⠏⠄⢀⣀⣀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠄⠄⠄
    # ⠄⠄⠄⠄⢀⡀⠄⠄⠄⠄⠄⢀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣤⠈⠇⠄⠐⢛⣭⣽⣿⣿⣿⠁⠰⣿⣿⣿⣟⣻⣿⣦⠄⢻⡿⠿⣿⣿⣿⣿⣿⣿⡿⠯⠄⠄⠄
    # ⡀⠄⠄⠄⠘⠄⠄⠄⠄⠄⠄⠈⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠃⣠⠄⠄⠄⠋⢽⣿⣿⡿⠟⠄⠄⣿⣿⣿⣿⣿⠿⠿⠄⠸⠧⣶⣿⣿⣿⣿⣿⣛⠑⠄⠄⢀⠄
    # ⣧⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠉⠁⠄⠄⠐⠂⣿⡟⣿⣿⣷⣿⢼⠥⣏⡄⢀⢀⠄
    # ⣿⣿⡄⠄⣦⣀⡀⠄⠄⡀⣀⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡴⠄⡀⢀⣠⡶⢃⣀⣀⣀⣀⣳⣦⣀⡀⠄⣼⣿⣟⠉⢺⠿⢿⢿⠿⡿⠟⠾⠇⠡⠄⠄
    # ⣿⣿⣿⡠⡿⣿⣟⠟⠛⠛⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠄⠘⠄⢘⣯⢟⣀⣀⣼⣿⣿⣿⣇⣘⢿⣿⣿⣿⣿⣧⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
    # ⣿⣿⣿⣧⣤⣦⣴⣶⣤⣦⣴⣴⣴⣴⣴⣶⣦⣶⣶⣶⣷⣶⣶⣶⣶⣶⣿⣾⣷⡆⠄⠄⣈⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣶⣶⣶⣿⣿⣿⣶⣶⣶
    # ⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣁⠄⠄⢿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠁⠠⣼⣷⣦⣼⣿⣿⡍⠉⠉⠉⠉⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠟⠛⠋⠉⠉⠄⠄⠄⠄⠠⠶⣾⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠋⠄⠄⠄⠄⠄⠄⠄⡀⢀⣀⣀⡸⢤⠄⡠⢀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⣿⡟⠋⠁⢀⠄⣶⣾⣤⣥⣶⣿⣧⠂⣲⢡⣿⣿⣿⣿⣧⣴⣬⣿⣿⡿⠋⢁⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⡟⠶⣶⣾⣾⣶⣿⣿⣿⣿⣿⣿⣿⣫⣽⣾⣿⣿⣿⡿⣿⣿⣿⠛⠁⢀⣴⡞⠋⠉⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣦⣙⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⢋⠄⠄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠋⠄⢰⡟⣻⣿⠒⠚⠒⠄⣀⣽⣿⣿⣿⣿⣿⡿⠟⠛⠛⠃⠈⠛⣿⣿⣿⣷⡝⢿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⢋⣿⣿⣶⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠃⠄⢠⣟⣿⣿⣿⣶⣿⣿⣶⣤⡀⠘⣿⠟⠋⣀⣤⣤⣶⣶⣤⠐⠄⠈⢻⣿⣿⣿⣷⣬⡻⢿⣿⣿⣿
    # ⡿⣃⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣤⣄⣴⣿⣿⣿⣿⣿⣽⠠⠄⠄⠄⠻⣿⣿⣿⣿⣿⣿⣿⣻⣿
    # ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠄⠄⢀⣰⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠄⠄⠄⠄⠄⠘⣿⣿⣿⣿⣿⣿⣿⣷
    # ⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠛⠁⠄⠄⠄⢀⣼⣿⣿⣿⠟⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠄⠐⠂⠄⠄⠄⠸⣿⣿⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣯⣿⣿⡿⠿⠛⠛⠉⣠⣴⣦⣤⣵⠁⠄⠄⠄⠄⠄⣠⣾⣿⡟⠁⠄⠄⠄⠸⠗⠈⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⣿⣿⣿⣿
    # ⣿⠿⢋⣉⣥⣤⣤⣦⣲⣶⣾⣿⣿⣿⣿⣿⣄⣀⣀⣤⣤⣶⣿⣿⣁⣀⡀⡀⣀⣄⣆⣄⣀⡀⠄⠄⢈⣿⡿⠛⠉⠉⠉⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⣿⣿⣿⣿⣿
    # ⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣀⣤⣤⣤⣤⣤⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿
    # ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⢫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⡀⠄⠄⣀⠄⠄⢀⣿⣿⣿⣿⣿




















# #B########B#B##################################&&&&&&&&########&#########&######&#####&##&&######&&&
# BBBBBBBBBBBBBBBBBB#BBBBBBBB#BBBBBBBBBBB#####################&#######################################
# GGGGGPGGPGGGGGGPGGGGGGGGGGGGGGGGGGGGGBBBBBBBBBBBBBB##BG55YY555555YY55PPPGGBBGGGGBBBBBBBBGBBBBBBGGGGG
# PPPPPP55P5555P555PP55P5555Y555555Y55PPPPGGGPGGPPPP5YJJY555YJYYYY55YYYYJJJJYJJJJY5PPGGGGGGGGGGGGGPPPP
# 5YYYYY5YYYYYYYY5YYYYYYYJJJJJJYYJJJJJJYJYYY5555Y5P5YY5PGBGPPGPPG5GGGGPPPGGGGP5YJ?JY5PPPPPPPPPPPP55555
# YYYYYYYYYYYYJJYYYYJJJJJJJJJJJJJJJJJJJJJYYY55555PGGGBBBGGGGBBBGGGBBBBGGGBB#BBBBG5J?JJYJJJJYY5YYJ?????
# JJJJ?JJ?J???777777?77777777777777!7777!7777775PGGGGGGGBGBB#############&&#BBGGGGPY????777??JJ???77!!
# !!!~~~!~~~~~~~~~~^~^~~~~~^^^^^^^^^^^^^^^^^^~JY5PGGBBBBBB##B#####&&&###&&&&&BBGGGBGJ777??7?7??????7!!
# !!~~~~~~~^~~^~^^~~^^^^^~^^^^^^^^^^^^^^^^^^^7YPPPPGGP5GP555YYGB##&&&&&&&&&&&&####BG5J????????7?????!!
# !!~~~~~~~~~~~~~~~^^~~^~~^^^^^^^^^^^^^^^^^^~?5GGGBBBPY7~~~~~~!?JYPGGGPPGBGB&&&&&#BBGP??JJJ????????7!!
# !!!!~~~~~~^~~~~~~^~~^~~~~^^^^^^^^^^^^^^^^^^~5###&#P7~^~^~~~~^^^^~~~~~~~~^~?B&&&&&&#5YYYYYYYYJJJJ?77!
# !!~!~~~~~~~~~~^~~~~~^~^^^^^~^^^^^^^^^^^^^^^^!B&&#P7~~~~^~~~~~~~~~^^~~~~^~~!?G&&&&&B555555P5555YJ?7!!
# !!~~~~~~~~~~~~~~~~^~^~~^^^^^^^^^^^^^^^^^^^^^:7&#GY~^^^^^^^^^~^^^~^^^^^^^^~!JG&&@&&G55555PPPP55Y?!!!!
# ~~~~~~~~~~~~~~~~^~^~~~~~^^^^^^^^^^^^^^^^^^^^:~##7^~!?JJJJJ???77~!!777????7~!JG&@&B555PP55PPPP5J7!!~~
# !~~~~~~~!!~~~~~~~~!~~~~~~^^^^^^^^^^^^^^^^^^^?~5Y^^!J555P#&&&GJ!7P#&&&#GGB#G!^7#@#55PPPPGPP555YJ?7777
# !!~~~!!JJ7!~~~~~~!?J!~~^~^^^^^^^^^^^^^^^^^^!Y77~^~~75GB#####P!^^J&&####B#BPJ~~PB?J5PPGPPP55YJJ?7??77
# ?!!~~!!!~~~~~~~~^^~!!~~^^^^^^^^^^^^^^^^^^^^!7J?~~^^~~7J5PP5JJ~^^!PGPPGGP55J??7J5GBPP55555YJJJJ????77
# P?!~~!!~~~^~~~^^^^~!~~^^^^^^^^^^^^^^^^^^^^^^!7~!~~~~~~^~~^~!!~^^~?7~!77!77!7?J?5PYY55YJYYJJJJJJ????7
# BB57!~77~~~~^^^^^~77!~^^^^^^^^^^^^^^^:^^^^^^~^^!7??7!~^^~7J~^^^^^7J?!~^^~7?JJYJJJJ55555YYJJYJYJJJ???
# ##B57!J5J?7!!!77?JJ?!~~~~~~^~~^^^^^^^^^^^^^^~~~7JY?????Y5Y??J777?J5GP5J???J555J!!Y5YYYYYJJJJJJ???777
# &&#GY?JY55YYYYYJJ??7!!~!~!~~~~~^^^^^^^^^^^^^~!7~?J??JY5Y7^^?GB&&&#57?5GG5YY55PY7!7!!!!!!~!~!!~~~~~~~
# &&&B5???J?J???777777!!!!!!!!!!7777!!!!7777?????7?77?JYJYPGGB#&&&&&&#BPPGGGP5555Y?7?77???7???????7???
# ##&#GPPPPPPPPPPP5PPPP5555PPPP55PPPPPGPPGGGGGGGGY7??JJYB&@@&@@@@@@@@@@@&BGGP5PGGGBBGGGGBBGGBGBBGBBB##
# 5B&&##B#######B#B#BB#BBBBBBBBBBBBBBB#BB##B###GY77?7J5G##BGGGBGB##&&@@@&&#GPG#################&###&&&
# 5#&&&##&&&###&&###################B######&##5!7JYJ77Y5P5YYYPB&&&&&##BB#BBGPB&&&&######&#####&&###&&&
# #&##################################BBBGGY?77?JJ5P5JYP55J?!~~~7???JYPGB##BGG##&&####################
# ##B#BBBB################&###BGG5J??!!!!~~^!?JJY55PPPGB##BGPPPGBBBGB##&&#BBPPB##&&############BB#####
# &#BB##B######&&##BP5YYJJ???7!~~~!!77777777?JJYY55PGGB###&&&@@@@@@@@@@&&##BGGP#&#&######BBB###BBBBBBB
# &#BBBBBBB###G5J?7~~~~!!!!!!77777JJJJJJJ????JY555PPGBBB#B#&&@@@@@@@@&&&&&#B##GG#&&&&&&#&##&##########
# &&&#BBBB#BPJ7~!7?JJJ??JJJJJJ?JJJYYYYYYYYJJ?YY5555Y77GGBBB##&&&&@@&&&&&&#####B55B&&&&#&&&&&&&&&##&#&&
# &&&&#B#BP?77??JJY55YYYYYYYYJ?JJY555Y5555YYJYYYY?!~?PGPPPBBBBB#########&&&##BBGPYY5G####&&####&&&&&&&
# &&&&&&BYJ5PPP5555PGP55Y5Y5YYYY555P55Y55PPYYJ?!~!YBGJ!~~!7JG#BBGGB##&&&&#####P5GP5JJJ5GB####&&&&&&&&&
# &&&&&G?!7?5GBBGGPPGGPPP5555YY55P5P555YY5PGY!^~JBB5P5JJY?~~!?B&@######&##BGGP7^75GP555YYPB#&&@&&&&&&&
# &&&&PJJ????5PBBBBGGBGPPPPP555PPPPPPP5555P5!~~Y&PYGB5?J55?77JPB&&#BBG5YJ?77!!!!!!JGGPPPPYJY5B&@@&&&&&
# &&&5?Y5555YYY5GB#BBBBGGGGP55PPGGGGPP5555?~^~JBPPBPGGBB&&&#BJ^~Y&#P?!!!?YPG5YYJ?!~7JPGPPP55JJ5G#&@@&&
# &#J?YY5PPGP5555PGGBB##BBBPPPPGGGPPGPPPJ!~~!75PGBBG##&&&#&&&&Y!!Y7~7YB##&&#GPPJ777!!?PGPPPPP55YY5B&&@
# GYY5GGBGGGGGBBBBBBB##&##BPGBBGGGPPP5J!~~~!?PB######&&#BB#&&&&#####&&#B#&&BGP5J7777!~75PPP5PPPPP5YY5G
# PGBBBBGGGPGB#&&&#&##&&&#GGBBBGGGP5J!~~~!75B######GB&#BGGBB#BB###&&@&&GGB&&&57?77!!!~~!YPGPGGGGGGPP5Y
# 5PPGBBB####BBB#&&&&&&&&#BBBGGGPJ7!~~~!!JPB&&#BGPP5P&BGGGGPGBBBBBB##&&&##&&@#?????!!~~~!?PBB#BBBBBGGP
# YYYPGBB##&&&##B#&#BBGGPYJ???77!!!!!!!7YG#&#G5J?JJY5GGGGGGGGGGGGBBBB#&&&&&@@5!!777??!!~!7YB##B##BBBBG
# BBGPP55GBB##BP5YJJ?JJ?J?JJ7!!!!!7!!7?5B#B5J?77!77?J7?YPPPGGGGPGGGGBBBB###&B!!~~~~!77!~!!7YG######BBG
# BBBGP5YJJJ?J????JY555555G577777777?YPBG5?777!!!77?7!!!77JJYPGGGGPP555P555J7!~~~~~~~!7~~!!7JG#####BBB
# Y5YJJJJJJYYYYY555PPP555G&5JJJY555PPGGGY??????JY5P5PPYJ?777?JPGY?!!!!~~~!!!~~~~~~~~~~7!!!!77JG##&BB##
# Y555555PP555555PPPGPPP5#&BGGGGPGGGBB#########&&&&&@@@&&&#BP55Y!!777?JJJJ?7!!!~~~~~~!!7!!!77?5BBB####
# GGPPGGPP555PP5PPPPPGGPP&&&##BGGG##B#&&@@@@&&&&&&&&&&&&&&&@@&####&&&&&&&&&BGY?77!!!!!7777777J5G5YPGGB
# BGGPGPP55Y5555P5555PGPG&&BBGP5JJBPP##&&&&##BBBB#&&#######&@&&&@@&&&&&@@&@@@&&#PJ???77??????JY55YY5GP