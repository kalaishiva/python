def process_order(item, quantity):
    try:
        price = {"masala": 20}[item] # in the place of item "[ginger]" will go but it is not same as masala. so it wont excequte
        cost =  price * quantity
        print(f"The masala chai total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Quantity must be in number")

process_order("ginger", 2) # ginger is given, not the masala
process_order("masala", "two") # two is written ..it should be in number like 1, 2....they print multiple type we have to fix it
process_order("masala", 2) # this is the correct formate of key, value pair
    