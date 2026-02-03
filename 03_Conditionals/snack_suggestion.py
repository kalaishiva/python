#  Cafe wants a program that suggest a snack. if a customer asks for cookies or samosa, it confirms the order. 
# otherwise say its not available
# task 1. Take snack input
# if it is cookies or samosa, confirm the order .....else show unavailablity





snack = input("Enter your snack : ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great choice!, we will serve your {snack} soon")
else:
    print(f"Sorry, we only have cookies and samosa")