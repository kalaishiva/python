order_amount = int(input("Enter your order amount: "))

delivery_amount = 0 if order_amount > 300 else 30

print(f" Your delivery amount is : {delivery_amount}")

