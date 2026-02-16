class Chai:  # always capital letter
  pass
print(type(Chai))

class ChaiTime:
  pass

ginger_tea = Chai() # ginger tea is getting the variable value from the chai.  the object is created
print(type(ginger_tea)) # It an object of the type class Chai
print(type(ginger_tea) is Chai) # true
print(type(ginger_tea) is ChaiTime) # false
