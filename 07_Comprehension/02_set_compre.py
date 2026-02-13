favourite_chais = [
    "Masala chai", "Green Tea", "Masala chai", "Lemon Tea", "Green Tea", "Elachi chai"
]

unique_chai = {chai for chai in favourite_chais}
print(unique_chai)

# Anothe example

recipes = {
    "Masala chai": ["ginger", "cardomon", "clove"],
    "Elachi chai": ["cardomon", "milk"],
    "Spicy chai": ["ginger", "black pepper", "clove"],
}

unique_spices = {spice for ingredient in recipes.values() for spice in ingredient}
print(unique_spices)