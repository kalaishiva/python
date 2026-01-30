is_boiling = True
stir_count = 5
total_action = stir_count + is_boiling # upcasting
print(f"Total action : {total_action}")


milk_present = 0     # no milk
print(f"Is there milk? {bool(milk_present)}")

water_hot = True
tea_added = False

can_server = water_hot and tea_added
print(f"Can server tea {can_server}")