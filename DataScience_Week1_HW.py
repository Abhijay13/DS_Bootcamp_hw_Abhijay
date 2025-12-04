# Homework

# 1. Count vowels in a word
word = input("Enter a word: ").lower()
vowels = "aeiou"
count = sum(1 for letter in word if letter in vowels)
print("Number of vowels:", count)

# 2. Print each animal in all caps
animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for animal in animals:
    print(animal.upper())

# 3. Print numbers 1 to 20 with odd/even label
for i in range(1, 21):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")

# 4. Check if a string is a palindrome
word = input("Enter a word to check palindrome: ").lower()
if word == word[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

# 5. Function to sum two integers
def sum_of_integers(a, b):
    return a + b

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
print("The sum is:", sum_of_integers(num1, num2))
