# What parameters should be sent to the range constructor, to produce a range with values:
# a) 50, 60, 70, 80
# b) 8,6,4,2,0,-2,-4,-6,-8

# A Solution typical question tend to test the concepts of the algorithms 
def anyInA():
    theList = []
    for i in range(50,81,10):
        value = i
        theList.append(value)
    return theList

# B Solution
def anyInB():
    theList = []
    for i in range(8,-9,-2):
        value = i
        theList.append(value)
    return theList

# Alternative B Solution
def anyInC():
    theList = []
    for i in range(8,-10,-2):
        value = i
        theList.append(value)
    return theList

def main():
    a = anyInA()
    b = anyInB()
    print(a)
    print(b)

main()