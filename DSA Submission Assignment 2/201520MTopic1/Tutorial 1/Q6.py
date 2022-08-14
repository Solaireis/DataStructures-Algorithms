# Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order.
# (NOTE: A user can indicate end of input by typing ctrl-D).
# (HINTS: You will need to use the try and except blocks to capture the exception.
#  Use a list to store all the lines then try using the built-in reverse()
# function to reverse the order.)

lines = []

try:
    while True:
        line = input("Enter a line(ctrl-D to stop): ")
        lines.append(line)

except EOFError as e:
    lines.reverse()
    print(" ")
    for line in lines:
        print(line)

#alternative method (Isaac solution)
while True:
    try:
        line = input("Enter a line(ctrl-D to stop): ")
        lines.append(line)

    except EOFError as e:
        lines.reverse()
        print(" ")
        for line in lines:
            print(line)