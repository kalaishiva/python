def serve_chai():
    yield "Cup 1: Masala chai" # Yield key word used for generator
    yield "Cup 2: Elaichi chai"
    yield "Cup 3: Ginger chai"

stall = serve_chai()

for cup in stall:
    print(cup)

# Normal function example

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

# Generator function

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()

print(next(chai)) # gives only first "Cup 1"
print(next(chai))
print(next(chai))
# print(next(chai)) # gives error because only 3 values available