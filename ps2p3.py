#input phase
totalpay = float(input("Enter total pay: $ "))
workers = int(input("Enter number of workers: "))

#process phase
indvpay = totalpay / workers

#output phase
print("Individual pay received: $", indvpay)