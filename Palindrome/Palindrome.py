userString = str(
    input("This program checks if a string is a palindrome. Enter a string: ")
)

userStringReversed = userString[::-1]

if userString.upper() == userStringReversed.upper():
    print(userString, "is a palindrome.")
else:
    print(userString, "is not a palindrome.")
