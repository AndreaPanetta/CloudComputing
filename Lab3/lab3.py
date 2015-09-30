#Program to detect if a word is a palindrome or not

pal_string = raw_input("Enter a string: ")

def reverseString(aString):
  return aString[::-1]

if pal_string == reverseString(pal_string):
  print("True")
else:
  print("False")

