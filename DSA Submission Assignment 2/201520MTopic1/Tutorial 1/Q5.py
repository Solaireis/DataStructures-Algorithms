# Write a short Python function num_vowels(text) 
# that counts the number of vowels in a given character string.

def num_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in word:
        if i in vowels:
            count += 1
    print("Number of vowels:", count)

#alternative method (teacher solution)
def num_vowels2(text):
    total = 0
    for ch in text.lower():
        if ch in 'aeiou':
            total += 1
    return total

#alternative method 2 (joshua solution)
def num_vowels3(txt):
    txt = txt.upper()
    vowel_count=0
    vowels="AEIOU"
    for letter in txt:
        if letter in vowels:
            vowel_count+=1
    return vowel_count

word = input("Enter a word: ")
num_vowels(word)
