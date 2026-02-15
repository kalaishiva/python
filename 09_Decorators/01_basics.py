from functools import wraps

def my_decorator(func):  #we are passing function
    
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func() #whatever the function accepting as a param. we are execute them.
        print("After function runs")
    return wrapper


@my_decorator # this says whatever coming in the next line, will be wrapped up. if we remove it cant able to show the before and the after message.
def greet(): # this is the func paramerte passing into the function
    print("Hello from decorators class from chaicode")

greet()
print(greet.__name__) # if we want to know the name..use the dunder __name__...it will give you wrapper as a output.
