"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Original sting
text = "programming"
# reversed using slincing
reversed_text = text[::-1]
# print the reversed sting
print("Reversed string:", reversed_text)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
# Get user's full name
full_name= input("Enter full name: ")
# Split the name into parts
name_parts = full_name.split()
# Get the initials and convert to uppercase
initials = ""
for part in name parts:
    initials += part[0].upper() + "."
# print the results
print("Initials:", initials)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
# Get input from the user
text = input("Enter a word:")
# Convert to lowercase for case-insensitive
text_lower = text.lower()
# Check if the string is equal to its reversed
if text_lower ==text_lower[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Ask the user to enter a sentence
sentence = input("Enter a sentence:")
# Split the sentence into words
words = sentence.split()
# count the number of words
word_count = len(Words)



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
# Original string
text = "This is a string and it is an example."
# Replace 'is' with 'was'
modified_text = text.replaced("is","was")
# Print the modified string
print("Modified string:", modified_text)
