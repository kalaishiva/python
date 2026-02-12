menu = [
    "Masala Chai",
    "Iced Lemon tea",
    "Green tea",
    "Iced Peach tea",
    "Ginger chai"
]

#iced_tea = [my_tea for my_tea in menu if "Iced" in my_tea]
iced_tea = [my_tea for my_tea in menu if len(my_tea) >9 ] # to get the length

print(iced_tea)