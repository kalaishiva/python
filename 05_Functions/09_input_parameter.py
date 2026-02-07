chai = "Ginger chai"

def prepare_chai(order):
    print("Prepare ", order)

prepare_chai(chai)


# examples

chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42   #we can change the position by this

edit_chai(chai)
print(chai)

# another examples

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low")  #Positional
make_chai(tea="Green", sugar="low", milk="no")

# examples for (*) = args(arguments) and (**) =kwargs(keywordarguments)

def special_chai(*ingredients, **extras):
    print("Ingredients = ", ingredients)
    print("Extras = ", extras)

special_chai("Cinnamon", "Cardmom", sweetener="Honey", foam="Yes")


# examples
 
def chai_order(order=[]):
    order.append("Masala")
    print(order)

chai_order()
chai_order()
   