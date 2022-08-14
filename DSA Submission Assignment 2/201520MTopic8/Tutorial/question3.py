import stackadt as stack

def transfer(S, T):
    while not S.isEmpty():
        T.push(S.pop())

# Test code
S = stack.Stack()
T = stack.Stack()

for i in range(10, 90, 10):
    S.push(i)

print('Before')
print('S: ', S._theItems)
print('T: ', T._theItems)
print(' ')
transfer(S, T)
print('After')
print('S: ', S._theItems)
print('T: ', T._theItems)
print(' ')