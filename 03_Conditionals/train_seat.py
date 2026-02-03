#Building a tickedt info for railway app. Based on seat type, show its feature
# task 1. input "sleeper/ AC/ general/ luxury" 2. Match using match case 3. unknown..show as "invalid"








seat_type = input("Enter your seat type (sleeper/ AC/ general/ luxury)").lower()

match seat_type:
    case "sleeper":
        print(f"Sleeper, Non-AC but beds are available")
    case "ac":
        print(f"AC comfy ride")
    case "general":
        print(f"General, chepeast option")
    case "luxury":
        print(f"Luxury, Premium seats with meals")
    case _:
        print(f"Invalid seats")