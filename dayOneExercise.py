# print ("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
# print ("2. Knead the dough for 10 minutes.")
# print ("3. Add 3g of Salt.")
# print ("4. Leave to rise for 2 hours.")
# print ("5. Bake at 200 degrees C for 30 minutes.")




# print ("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.\n2. Knead the dough for 10 minutes.\n3. Add 3g of Salt.\n4. Leave to rise for 2 hours.")
# print ("5. Bake at 200 degrees C for 30 minutes.")

print("Hello" + " World!")

print("Hello" + " " + input("your name")+"!")

#calculate no of characters in user input
#userInputLength=len((input("your name: ")))
#print(userInputLength)
print(len((input("your name: "))))
print("length is: " + str(len((input("your name: ")))))

#using variable print name and length

usrName = input("your name: ")
length = len(usrName)
print("User name is " + usrName + " and length is: " +str(length))


#exercise three
glass1="milk"
glass2="juice"
glass3=glass1
glass1=glass2
glass2=glass3
print(glass1 +" " + glass2)