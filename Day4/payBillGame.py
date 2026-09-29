import random
friends = ["Amy", "Eva", "Ron", "Shane"]

print(friends[0])
print(friends)

#add code to randomly pick friend from list to pay bill
#using random choice

print("Who will pay?? " + random.choice(friends))

# using randint

random_number = random.randint(0,3)
print(random_number)

print(friends[random_number] + " will pay the bill")