def main():
    print(sum(10))

def sum(x):
    if x == 1: # base case first
        return 1
    else:
        return x + sum(x-1) # else do recursion case
#call tree is important
main()