# Function for nth Fibonacci number
def Fibonacci(n):

    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 0:
        return n

    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

    #Other Solution 
    # assert n >= 0, "Fibonacci number is not defined for negative numbers"
    # if n == 0 or n==1:
        #print(n)
        #return n
    # else:
        #return Fibonacci(n-1) + Fibonacci(n-2)



# Driver Program
print(Fibonacci(21))
for i in range(22):
    print(Fibonacci(i))