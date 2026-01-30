# Tuples

masala_spices = ("cinnamon", "cloves", "cardomon") # these are the values

(spice1, spice2, spice3) = masala_spices # values are add into variables

print(f"Main masala spices : {spice1}, {spice2}, {spice3}" )


# we can directly assign the variables to the value
 
ginger_ratio, cardomon_ratio = 2, 1       
print(f"Ratio of Ginger :{ginger_ratio} and Ratio of Cardomon : {cardomon_ratio}")     

# Interchange the values
ginger_ratio, cardomon_ratio = cardomon_ratio, ginger_ratio
print(f"Ratio of Ginger :{ginger_ratio} and Ratio of Cardomon : {cardomon_ratio}")     


# membership testing
print(f"Is ginger in masala spices ? {'ginger' in masala_spices}")

print(f"Is cloves in masala spices ? {'cloves' in masala_spices}")