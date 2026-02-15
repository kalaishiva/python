def chai_customer():
    print("Welcome ! What chai would you like ?")
    order = yield # we wait for the order
    while True:
        print(f" Preparing: {order}")
        order = yield # it is paused again...if another order placed this is used

stall = chai_customer()
next(stall) # start the generator

stall.send("Masala chai")
stall.send("Lemon chai")
