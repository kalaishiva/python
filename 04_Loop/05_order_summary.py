#Preparing order summary with customer names and their total bills.bills
#Task: one for name and one for bill.bills
 #   print [name] and paid [amount]



names = ["Kalai", "Shiva", "Vani", "Shivani"]
bills = [100, 280, 938, 243]

for person, amount in zip(names, bills):
    print(f"The bill amount for  {person} has to pay {amount} Rs")