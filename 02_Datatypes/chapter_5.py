import sys
from fractions import Fraction     # do fractions upto 6  numbers
from decimal import Decimal        # in documentation we can check for decimals

ideal_temperature = 95.5
current_temperature = 95.49

print(f"Ideal temperature {ideal_temperature}")
print(f"current temperature {current_temperature}")
print(f"Difference temperature {ideal_temperature - current_temperature}")

print(sys.float_info) #gives the float information