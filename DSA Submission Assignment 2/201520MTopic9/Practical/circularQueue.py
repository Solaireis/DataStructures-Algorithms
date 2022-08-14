# Implementation of the Queue ADT using a circular array.
class Queue:
    # Creates an empty queue.
    def __init__( self, maxSize ) :
        self._count = 0
        self._front = 0
        self._back = maxSize - 1
        self._qArray = [None] * maxSize
    # Returns True if the queue is empty.
    def isEmpty( self ) :
    # Returns True if the queue is full.
        return self._count == 0

    def isFull( self ) :
    # Returns the number of items in the queue.
        return self._count == len(self._qArray)

    def __len__( self ) :
    # Adds the given item to the queue.
        return self._count

    def enqueue( self, item ):
        assert not self.isFull(), "Cannot enqueue to a full queue."
        maxSize = len(self._qArray)
        self._back = (self._back + 1)%maxSize
        self._qArray[self._back] = item
        self._count += 1
    # Removes and returns the first item in the queue.
    def dequeue( self ):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        item = self._qArray[self._front]
        maxSize = len(self._qArray)
        self._front = (self._front + 1) % maxSize
        print(self._front)
        self._count -= 1
        return item

    # Return the content of the queue (with array index in square
    # brackets].
    def __str__( self ) :
        maxSize = len(self._qArray)
        outStr = ''
        for i in range(self._count):
            outStr += ('[' + str((self._front + i) % maxSize) + ']:')
            outStr += (str(self._qArray[(self._front + i) % maxSize]) + ' ')
        return outStr

if __name__ == "__main__":
    myQueue = Queue(5)
    myQueue.enqueue(293)
    myQueue.enqueue(564)
    myQueue.enqueue(8)
    myQueue.enqueue(9)
    myQueue.enqueue(10)


    print("testing with a queue of max size of 5 items ")
    print("after enqueing 5 items to an empty queue")
    print(myQueue)
    myQueue.dequeue()
    print(myQueue)
