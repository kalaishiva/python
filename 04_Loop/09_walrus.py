value = 13

if remainder := value % 5:
    print(f"Not divisible, remainder is {remainder}")


# next example

available_size = ["small", "medium", "large"]

if (requested_size := input("Enter your tea size: ")) in available_size:
    print(f" Serving {requested_size}")
print(f" {requested_size} size is not available ")

# next example
flavors = ["Ginger", "Lemon", "Mint", "Masala"]

while (flavor := input("Choose your flavor : ")) not in flavors:
    print(f"Sorry {flavor} is not available")

print(f"You choose {flavor} chai")