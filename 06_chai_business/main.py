# different ways of import from folders


# first way
import recipes.flavors

print(recipes.flavors.ginger_chai())

# second way
from recipes.flavors import elachi_chai, ginger_chai

print(ginger_chai())

# Thirs way - but usually avoid this
from .recipes.flavors import ginger_chai

# how to convert the folder into the python package

# __init__.py 
# this __init__.py help to convert folder into the python package