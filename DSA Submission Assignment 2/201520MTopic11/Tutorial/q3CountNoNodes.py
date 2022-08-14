# Counts the number of nodes in Linked List recursively # given 'node' as starting node.
def getCountRec(self, node):
    if (node is None): # Base case 
        return 0
    else:
        return 1 + self.getCountRec(node.next)
        
# A wrapper over getCountRec()
def getCount(self):
    return self.getCountRec(self._head)