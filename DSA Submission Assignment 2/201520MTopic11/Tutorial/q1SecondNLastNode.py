# Question 1 of tutorial solution #Find second last node in the linked list.
def findSecondLastNode( self ): # Initialise curNode pointer 
    curNode = self._head
    # If the list is empty or contains less than 2 nodes
    if curNode is None or curNode.next is None: 
        return None
    # Traverse the linked list
    while curNode is not None:
    # If the current node is the second to last node,
        # return current node
        if curNode.next.next is None: 
            return curNode
        # If not, move to the next node
        curNode = curNode.next