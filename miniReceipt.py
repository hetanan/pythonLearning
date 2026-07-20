item_price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
tax_rate = float(input("Enter tax rate: "))
#
# item_price = float(item_price)
# quantity = int(quantity)
# tax_rate = float(tax_rate)

sub_total = float(item_price * quantity)
tax = float(sub_total*tax_rate)
total = float(sub_total + tax)

# print("Subtotal: " + str(sub_total))
# print("Tax Rate: " + str(tax))

print(f"Subtotal:  {sub_total}\nTax:  {tax}\nTotal:  {total}")

