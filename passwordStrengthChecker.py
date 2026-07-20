# check password strength


print("Welcome to password strength checker!")

user_password = input("Please enter your password: ")
print (user_password)
user_password_length = len(user_password)
has_min_length = user_password_length >= 8
has_digit = any(char.isdigit() for char in user_password)
has_upper = any(char.isupper() for char in user_password)
has_lower = any(char.islower() for char in user_password)
has_symbol = any(char in '!@#$%^&*' for char in user_password)

is_strong = has_symbol and has_upper and has_lower and has_digit and has_min_length

#check strength logic

if is_strong:
    print("Your password check passes!")
else:
    print("Your password check fails!")
    if not has_digit:
        print("Digit missing")
    if not has_upper:
        print("Uppercase missing")
    if not has_lower:
        print("Lowercase missing")
    if not has_symbol:
        print("Symbol missing")
    if not has_min_length:
        print("Minimum length missing")


# if(user_password == ""):
#     print("Please enter your password")
# elif(user_password_length < 8):
#     print("Your password must be at least 8 characters")
# else:
#     for (i in range(user_password_length)):
#         if(any(char.isdigit() for char in user_password[i])):
#             print("has digit")
