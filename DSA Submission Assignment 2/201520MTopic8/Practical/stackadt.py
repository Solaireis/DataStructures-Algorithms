# Implementation of the Stack ADT using a Python list.
class Stack:
    # Creates an empty stack. 
    def __init__( self ):
        self._theItems = list()
    # Returns True if the stack is empty or False 
    # otherwise
    
    def isEmpty( self ):
        # Returns the number of items in the stack.
        return len(self) == 0
    def __len__ ( self ):

    # Returns the top item on the stack without # removing it.
        return(len(self._theItems))

    def peek( self ):
        assert not self.isEmpty(), \
            "Cannot peek at an empty stack"
        # Removes and returns the top item on the stack.
        return self._theItems[-1]

    def pop( self ):
        assert not self.isEmpty(), \
            "Cannot pop from an empty stack"
        # Push an item onto the top of the stack.
        return self._theItems.pop()

    def push( self, item ):
        self._theItems.append(item)

if __name__ == "__main__":
    mystack = Stack()
    prompt = "Enter a number: ctrl d to end "
    value = int(float(input(prompt)))
    while True:
        try:
            mystack.push(value)
            value = int(float(input(prompt)))
        except EOFError:
            break

    print("The stack:")
    print("len",len(mystack))
    while not mystack.isEmpty():
        value = mystack.pop()
        print(value)
    print("The stack is empty.")    
    print("len:",len(mystack))