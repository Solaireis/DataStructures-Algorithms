import theQueue as queue
import stackadt as stack

def reverseQueue (Q):
    S = stack.Stack()
    while not Q.isEmpty():
        S.push(Q.dequeue ())
    while not S.isEmpty () :
        Q.enqueue (S.pop () )

# Test code
myQueue = queue.Queue()
for i in range (10,60,10) :
    myQueue.enqueue(i)
print ('The contents of the queue (BEFORE REVERSING) : ')
print (myQueue._qList)
reverseQueue (myQueue)
print('\n')
print ('The contents of the queue (AFTER REVERSING) : ')
print (myQueue._qList)