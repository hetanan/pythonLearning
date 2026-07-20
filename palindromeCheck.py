#doesn't clean string for any leading spaces
user_string = input("enter string: ")
reversed_string = user_string.lower()[::-1]
print(reversed_string)

if reversed_string == user_string:
    print(user_string + " is a palindrome")
else:
    print(user_string + " is not a palindrome")