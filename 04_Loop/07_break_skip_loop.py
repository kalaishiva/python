# Some chai flavor is out of stock
# you want to skip those and stop entirely if someone request a restricted flavor
# Task 1. Skip if the flavor is "out of stock"
#.     2. Break if the flavor is "Discontinued"


flavors = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Thulsi"]

for flavor in flavors:
    if flavor == "Out of Stock":
        continue
    if flavor == "Discontinued":   
       print(f"{flavor} item found")
       break
    print(f"{flavor} item found")

print(f"Outside of the loop")


#continue = it will skip the one loop
#break = it will stop the loop, no further steps