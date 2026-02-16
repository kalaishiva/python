class Chaicup:
    size = "medium"

    def describe(self): # To all the property refer like size
        return f"A {self.size} chai cup"
    
#first object created  
cup = Chaicup() # create an object from the class
print(cup.describe()) 

print(Chaicup.describe(cup)) 


#Another object created
cup_two = Chaicup()
cup_two.size = "small"
print(cup_two.describe())

print(Chaicup.describe(cup_two)) 
