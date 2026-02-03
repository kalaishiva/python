# in tea stall different price for different cup size..write a program tha calculate the price base on size.
# Task input small/ medium/ large ...if s = 10, m= 15, l=20..if invalid show "unknown cup size"



cup = input("Choose your cup size : (small/ medium/ large)").lower()

if cup == "small":
    print(f"Price is 10 rupees")
elif cup == "medium":
    print(f"Price is 15 rupees")
elif cup == "large":
    print(f"Price is 20 rupees")
else:
    print(f"Unknown cup size")
