chai_menu = {"masala": 30, "ginger": 40}

try:
   chai_menu["elachi"] # if there is an error it will exciqute the remaining code
except KeyError:
   print("The key that you are trying to access does not exists")

print("Hello chai code")