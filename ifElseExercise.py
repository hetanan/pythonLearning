##if else example1
#
# print("Welcome to rollercoaster!")
# height = int(input("Enter your height in cms: "))
#
# if height >= 120:
#     print("You can ride the roller coaster!")
# else:
#     print("You cannot ride the roller coaster!")
#
# # if else example 2 find even number
# print("Welcome to Odd Even finder!")
# user_num = int(input("Enter any +ve number: "))
#
# if user_num % 2 == 0:
#     print(f"The number is {user_num} even number")
# else:
#     print(f"The number is {user_num} odd number")

#if else nested example

print("Welcome to rollercoaster!")
height = int(input("Enter your height in cms: "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("Enter your age: "))
    if age > 18 and age < 45:
        bill = 12
        print("You are eligible for an adult ticket")
    elif age >=12 and age <= 18:
        bill = 7
        print("You are eligible for youth ticket")
    elif age >= 45 and age <= 55:
        print("you can ride free!!")
    else:
        bill = 5
        print("You are eligible for child ticket")
    wants_photo = input("Do you want photo? Type y for Yes and n for No.")
    if wants_photo == "y":
        # bill = bill + 3
        bill+= 3
        print(f"Your final bill is: ${bill}")
    else:
        print(f"Your final bill is: ${bill}")
else:
    print("You cannot ride the roller coaster!")



# bmi check

# weight = 44
# height = 1.85
# bmi_value = (weight / (height*height))
# bmi_final = round(bmi_value,2)
# print(bmi_final)
#
# if bmi_final <18.5:
#     print("Underweight")
# elif bmi_final >= 18.5 and bmi_value <=24.9:
#     print("Normal")
# elif bmi_final >= 25 and bmi_value <= 29.9:
#     print("Overweight")
# else:
#     print("Need to see doctor")
#
