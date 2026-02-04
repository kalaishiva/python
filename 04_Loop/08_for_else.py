staff = [("Ramya", 13), ("Sunitha", 15), ("Shivani",12)]


for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print(f"They are not eligible to manage the staff")