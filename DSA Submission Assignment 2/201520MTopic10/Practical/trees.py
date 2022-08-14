from theQueue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    # Creates an initially empty BST
    def __init__(self): 
        self._root = None 
        self._size = 0
        # Returns the total number of elements in the BST
    def __len__(self):
        return self._size
        
        # Insert new_node into the BST
    def insertNode(self, new_node): 
        if self._root is None:
            self._root = new_node
            self._size += 1
        else:
            self._recInsertNode(self._root, new_node)

    # Helper method to insert new_node into the BST recursively # from start_node
    def _recInsertNode(self, start_node, new_node):
        if start_node.data < new_node.data: 
            if start_node.right is None:
                start_node.right = new_node
                self._size += 1
            else:
                self._recInsertNode(start_node.right, new_node)
        else:
            if start_node.left is None:
                start_node.left = new_node
                self._size += 1
            else:
                self._recInsertNode(start_node.left, new_node)

    def preorderTrav(self):
        if self._root is None:
            print("tree is empty!")
        else:
            self._recPreorderTrav(self._root)
    
    def _recPreorderTrav(self, subtree):
        if subtree is not None:
            print(subtree.data, end=' ')
            self._recPreorderTrav(subtree.left)
            self._recPreorderTrav(subtree.right)
    
    def inorderTrav(self):
        if self._root is None:
            print("tree is empty!")
        else:
            self._recInorderTrav(self._root)
    
    def _recInorderTrav(self, subtree):
        if subtree is not None:
            self._recInorderTrav(subtree.left)
            print(subtree.data, end=' ')
            self._recInorderTrav(subtree.right)

    def postorderTrav(self):
        if self._root is None:
            print("tree is empty!")
        else:
            self._recPostorderTrav(self._root)
    
    def _recPostorderTrav(self, subtree):
        if subtree is not None:
            self._recPostorderTrav(subtree.left)
            self._recPostorderTrav(subtree.right)
            print(subtree.data , end=' ')
    
    def breadthfirstTrav(self):
        # Breadth-first traversal of the BST
        # Create a queue and add the root node to it
        myQueue = Queue()
        myQueue.enqueue(self._root)
        # Visit each node in the tree
        while not myQueue.isEmpty():
        # Remove the next node from the queue and visit it 
            node = myQueue.dequeue()
            print(node.data, end=" ")
                    # Add the two children to the queue

            if node.left is not None: 
                myQueue.enqueue(node.left)
            if node.right is not None:
                myQueue.enqueue(node.right)

# Test code
if __name__ == '__main__': 
    bst = BinarySearchTree()
    bst.insertNode(Node(60))
    bst.insertNode(Node(12))
    bst.insertNode(Node(90))
    bst.insertNode(Node(4))
    bst.insertNode(Node(41))
    bst.insertNode(Node(1))
    bst.insertNode(Node(100))
    bst.insertNode(Node(71))
    bst.insertNode(Node(29))
    bst.insertNode(Node(37))
    bst.insertNode(Node(84))
    bst.insertNode(Node(23))
    print("Size of BST: ", len(bst))
    print("\nPre-order Traversal of BST:") 
    print("===========================") 
    bst.preorderTrav()
    print("\n\nIn-order Traversal of BST:") 
    print("===========================") 
    bst.inorderTrav()
    print("\n\nPost-order Traversal of BST:") 
    print("===========================") 
    bst.postorderTrav()
    print("\n\nBreadth-first Traversal of BST:") 
    print("===========================") 
    bst.breadthfirstTrav()