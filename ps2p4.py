#input phase
make = input("Enter make: ")
model = input("Enter model: ")
msrp = float(input("Enter msrp amount: $"))
discount = float(input("Enter discount percent in decimal: "))

#process phase
amtoff = msrp * discount
dsctprice = msrp - amtoff

#output phase
print (" ")
print("Make: ", make)
print("Model: ", model)
print("MSRP: $", msrp)
print("Discount percent: ", discount)
print("Amount off: $", amtoff)
print("Discounted price: $", dsctprice)