class Chai:
    origin = "India" 

print(Chai.origin)    # when the variable go inside a class we call it as properties.


#add more property by putting dot(.) and add
Chai.is_hot = True
print(Chai.is_hot)

#create more object from class Chai
masala = Chai()
print(f"Masala Object : {masala.origin}")
print(f"Masala Object : {masala.is_hot}")


#we change to false
masala.is_hot = False

print("Class :", Chai.is_hot)
print(f"Changed Masala Object : {masala.is_hot}")

masala.flavor = "Cinnamon"
print(masala.flavor)


#Overview : Each object is actually having its own namespace which doesn't affect other objects. Also doesn't affect classes as well by default
 