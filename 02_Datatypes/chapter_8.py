ingredients = ["water", "tea powder", "milk"]
print(f"Ingredients in tea preparation {ingredients}")

ingredients.append("sugar")
print(f"Ingredients in tea preparation {ingredients}")


ingredients.remove("milk")
print(f"Ingredients in tea preparation {ingredients}")


# combine two of the list

spice_options = ["ginger", "cardomon"]
chai_ingrediant = ["water", "tea"]
chai_ingrediant.extend(spice_options)
print(f"Now chai ingrediant has : {chai_ingrediant}")

# insert at the particular option

chai_ingrediant.insert(2, "----milk----") # milk is inserted in the 2 position ...position starts with 0, 1, 2, 3, 
print(f"Now chai ingrediant has : {chai_ingrediant}")


# remove last added

last_added = chai_ingrediant.pop()
print(f"Now chai ingrediant has : {chai_ingrediant}")


# whole list can be reversed

chai_ingrediant.reverse()

print(f"Now reversed chai ingrediant has : {chai_ingrediant}")


# sorting
chai_ingrediant.sort()
print(f"Now sorted chai ingrediant has : {chai_ingrediant}")


# maximum
sugar_level = [1, 2, 3, 4, 5]
print(f"Maximum sugar level is = {max(sugar_level)}")
print(f"Minimum sugar level is = {min(sugar_level)}")



# Operator

base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]
full_liquid_mix = base_liquid + extra_flavour
print(f"Liquid Mix = {full_liquid_mix}")

strong_brew = ["black tea", "milk"] * 3
print(f"Strong brew : {strong_brew}")


raw_spice_data = bytearray(b"whiteTea")
raw_spice_data = raw_spice_data.replace(b"white", b"black")
print(f"Bytes = {raw_spice_data}")