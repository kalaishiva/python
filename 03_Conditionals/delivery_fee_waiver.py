# if the order amount is more tha 300 Rs delivery is free, otherwise cost is 30
# Task input order amount 
#use ternary operator to decide delivery fee


order_amount = int(input("Enter your order amount: "))

delivery_amount = 0 if order_amount > 300 else 30

print(f" Your delivery amount is : {delivery_amount}")

