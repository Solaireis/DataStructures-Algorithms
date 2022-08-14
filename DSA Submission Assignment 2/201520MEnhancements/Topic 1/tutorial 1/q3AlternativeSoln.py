# function_eg.py
def sum_of_squares(n):
    """
    returns the sum of the squares of all the positive integers smaller than or equal to n
    formula: (1/6)(n(n+1)(2n+1)) from https://www.wolframalpha.com/input?i=sum%28n%5E2%29
    """
    if (n < 0):
        raise ValueError("n must be positive")
    return (n * (n + 1) * ((2 * n) + 1)) // 6 # or sum(x**2 for x in range(n + 1))

def main():
    while (1):
        try:
            i = int(input("Enter a positive integer: "))
            print("Result:", sum_of_squares(i))
            break
        except ValueError:
            print("Invalid input, input must be a positive integer!")
            print()
    return 0

main()
print("\nEnd of program.")