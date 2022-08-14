# Concatenate 2 lists, L and M, given the first node of each list 
# # Assuming L and M are not empty
def concatTwoLists(firstNodeOfL, firstNodeOfM):
    # Initialise curNode to first node of L
    curNode = firstNodeOfL
    # Find the last node in list L
    while curNode.next is not None: 
        curNode = curNode.next
    # Link the last node in list L to first node in list M
    curNode.next = firstNodeOfM
    # Return the first node of L + M
    return firstNodeOfL