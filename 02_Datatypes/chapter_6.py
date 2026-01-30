chai_type = "Ginger tea"
customer_name = "Kalai"

print(f"Order for {customer_name} : {chai_type} Please !p")


# Strings
chai_description = "Aromatic and Bold"
print(f"First word : {chai_description[0:8]}")
print(f"Last word : {chai_description[12:]}")
print(f"Reverse word : {chai_description[::-1]}")

# Different Scripts
label_text = "Chai Spècial"
encoded_label = label_text.encode("utf-8")
print(f"Non encoded label = {label_text}")
print(f"Encoded label = {encoded_label}")

decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label = {decoded_label}")