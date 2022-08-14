
def sumDigits(n):
    if n == 0:
        return 0 
    else:
        return n % 10 + sumDigits(n // 10)

#testcode
print(sumDigits(368))

#base is important
#once call reach base you bounce up and then
#you add the values together
#once you reach base you stop
#or you draw the recurisve call tree
