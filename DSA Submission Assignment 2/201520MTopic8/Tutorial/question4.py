import stackadt as stack


def recEmptyStack(S):
    if S.isEmpty():
        return S
    else:
        a = S.pop()
        recEmptyStack(S)


# Test code
S = stack.Stack()

for i in range(10, 90, 10):
    S.push(i)

print('Before')
print('S: ', S._theItems)
recEmptyStack(S)
print('After')
print('S: ', S._theItems)