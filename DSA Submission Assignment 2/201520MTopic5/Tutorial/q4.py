#palindrome is a mirror spelling of the word 
# e.g. tops spot is a palindrome

def isPalindrome(aStr):
    if len(aStr) <= 1:
        return True
    return aStr[0] == aStr[-1] and \
        isPalindrome(aStr[1:len(aStr)-1]) # recursive call


while True:
    aStr = input('Enter a string: (q to quit): ')
    aStr = aStr.lower()
    
    aStr = ''.join(ch for ch in aStr if ch.isalnum())

    is_a_palindrome = isPalindrome(aStr)
    if aStr == 'q':
        break
    if is_a_palindrome:
        print('{} is a palindrome'.format(aStr))
    else:
        print('{} is not a palindrome'.format(aStr))
