def masala_chai():
    return "Here is your masala chai"
   # print("Here is your masala chai"). the output is none 

return_value = masala_chai()


print(return_value)


# example - one value
def sold_cups():
    return 123

total = sold_cups()
print(total)

# example -  return early from the function
def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over" #once the condition met the return, no further code executed.
    return "Chai is ready"

print(chai_status(0))
print(chai_status(3))

# Multiple value
def chai_report():
    return 100, 30 # we are returning for the sold and the remaining goods

sold, remaining = chai_report()

print("Sold : ",sold )
print("Remaining : ",remaining)


