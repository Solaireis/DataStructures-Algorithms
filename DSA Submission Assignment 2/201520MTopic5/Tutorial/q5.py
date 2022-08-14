def exp(x,n):
    y = 1
    for i in range(n):
        y *= x
    return y

def exp_recursive(x ,n):
    if n==0:
        return 1
    else:
        return x * exp_recursive(x,n-1)

    #go home do call tree

print(exp(2,8))
print(exp_recursive(2,8)) 