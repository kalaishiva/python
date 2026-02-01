chai_order = dict(type="Masala chai", size="Large", sugar=2 ) #dict() its a function
print(f"Chai order: {chai_order}")

#we often use {} for the dict()

chai_recipe = {}
chai_recipe["base"] = "black tea" 
chai_recipe["liquid"] = "milk" 

print(f"Recipe base : {chai_recipe["base"]}")

# delete
del chai_recipe["liquid"]
print(f"Recipe  : {chai_recipe}")

# membership test

print(f"Is sugar present in the order ? {'sugar' in chai_order}")

# it shows what is keys, values and items

chai_order = dict(type="Ginger chai", size="Medium", sugar=1 )

print(f"Order detail (keys) : {chai_order.keys()}")
print(f"Order detail (values) : {chai_order.values()}")
print(f"Order detail (items) : {chai_order.items()}")


#pop()

last_item = chai_order.popitem()
print(f"Removed last item : {last_item}")


#update 
extra_spices = {"cardomon": "crushed", "ginger" :"sliced"}
chai_recipe.update(extra_spices)

print(f" Updated Chai recipe : {chai_recipe}")


# we can get the size
chai_size = chai_order["size"]
print(f" Chai size : {chai_size}")

# get() method...incase if the type is not present we can include customised message that it is not found in the list
customer_note = chai_order.get("note", "NO note")
print(f" customer_note : {customer_note}")
