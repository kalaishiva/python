# Building simple app that register users
# You want to seperate concerns: getting input, validating it and saving it.
# Task:
# Write 1. register_user() that calls:
#     * get_input()
#     * validate_input()
#     *s ave_to_db()



def get_input():
    print("Getting user input")
    
def validate_input():
    print("Validating user input")
    
    
def save_to_db():
    print("Saving to database")
    
def register_user():
    get_input()
    validate_input()
    save_to_db()
    print(f"User registration complete")

register_user()