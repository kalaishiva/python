light_color = {"blue", "pink", "green"}
bright_color = {"red", "pink", "orange"}
 
all_colors = light_color | bright_color     # "|" this symbol is for union
print(f"all color : {all_colors}")          # same color donot repeat two times

common_colors = light_color & bright_color     # "&" this symbol is for intersection (or) common
print(f"common color : {common_colors}")



only_in_lightcolors = light_color - bright_color   # "-" this symbol is for only in one set and the common item is not displayed
print(f"Only in light color : {only_in_lightcolors}")