#input phase
stockts = input("Enter stock ticker symbol: ")
shares = float(input("Enter number of shares: "))
cost = float(input("Enter cost per share: $"))

#process phase
amtinvest = shares * cost

#output phase
print("Amount invested: $", amtinvest)
