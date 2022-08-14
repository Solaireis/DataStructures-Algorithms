# Implementation of the Queue ADT using a Python list.
class Queue:
    # Creates an empty queue. 
    def __init__( self ):
        self._qList = list()
    # Returns True if the queue is empty.
    def isEmpty( self ):
        return len( self ) == 0
    # Returns the number of items in the queue.
    def __len__( self ):
        return len( self._qList )
    # Adds the given item to the queue.
    def enqueue( self, item ):
        # Removes and returns the first item in the queue.
        return self._qList.append( item)
    def dequeue( self ):
        assert not self.isEmpty(), \
                "Cannot dequeue from an empty queue."
        return self._qList.pop( 0 )
        
        


if __name__ == "__main__":
    PROMPT = "Enter a number (Ctrl+D to end): "
    myqueue = Queue()
    value= int(float(input(PROMPT)))
    while True:
        try:
            
            myqueue.enqueue(value)
            value = int(float(input(PROMPT)))
        except EOFError:
            break
    print("The queue:")
    while not myqueue.isEmpty():
        value = myqueue.dequeue()
        print(value)
