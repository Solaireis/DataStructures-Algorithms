def move_discs(num,from_peg,to_peg,temp_peg): # 4 parameters und this is a recursive function (understanding the tutorial qn)
    if num > 0:
        move_discs(num-1,from_peg,temp_peg,to_peg) # it calls itself to execute the function 
        print('Move disc from peg',from_peg,'to peg',to_peg) #prints the current function parameters
        move_discs(num-1,temp_peg,to_peg,from_peg)
        # it calls itself to execute the function itself
        # in short this 1 function will create the recursive function youll need a tree to understand how it works 

move_discs(num=3,from_peg=1,to_peg=3,temp_peg=2)