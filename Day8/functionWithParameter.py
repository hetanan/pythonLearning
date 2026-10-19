# function without parameter

def greet():
    print("hello world")
    print("It is Monday")
    print("Bye")

greet()

# function with parameter and argument
def greet_with_name(name):
    print(f"Hello {name}")

userName = input("What is your name? ")
greet_with_name(userName)

# function with parameter and hardcoded argument

def greet_with_arg(name):
    print(f"Hello {name}")

greet_with_arg("Test")


