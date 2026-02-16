class Chai:
    temperature = "hot"
    strength = "strong"


cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"

print("After changing : ", cutting.temperature)
print("cup size is : ", cutting.cup)
print("Direct look into the class : ", Chai.temperature)

#use del i.e deletion operator
del cutting.temperature
del cutting.cup
print(cutting.temperature)
print(cutting.cup) # this value doesnt exist in the class.
# this shows attribute error. Chai object has no attribute cup. so we dont have fall back..if it is present that is shadowing..