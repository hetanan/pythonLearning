#need to letter = add code soon
#first version
# import random
#
# letters = ["a", "v", "r", "W", "T", "C"]
# numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
#
# print("Welcome to the password generator!")
# num_letters = input("How many letters would you like in password? ")
# num_numbers = input("How many numbers would you like? ")
# num_symbols = input("How many symbols would you like? ")
#
# # print (len(num_letters))
# # print(num_letters)
#
# random_letters = random.choices(letters, k=int(num_letters))
# random_numbers = random.choices(numbers, k= int(num_numbers))
# random_symbols = random.choices(symbols, k= int(num_symbols))
#
# password = random_letters + random_numbers + random_symbols
# print(password)
# final_password = "".join(password)
# print(final_password)


#second version using for loop

import random

letters = ["a", "v", "r", "W", "T", "C"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

print("Welcome to the password generator!")
num_letters = int(input("How many letters would you like in password? "))
num_numbers = int(input("How many numbers would you like? "))
num_symbols = int(input("How many symbols would you like? "))

password = ""
for letter in range(0, num_letters):
    password = password + random.choice(letters)

for num in range(0, num_numbers):
    password = password + random.choice(numbers)

for symbol in range(0, num_symbols):
    password = password + random.choice(symbols)

print(password)