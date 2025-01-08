# flavors = ["pistacho", "malaga", "vanilla", "chocolate"]
# prompt = "Choose your flavor: "
# print(flavors)
# while True:
#   choice = input(prompt)
#   if choice in flavors:
#     break
#   print(f"Sorry, '{choice}' is not a valir option.")
# print(f"You chose '{choice}'")

# ¿Cómo podemos mejorar?:
flavors = ["pistacho", "malaga", "vanilla", "chocolate"]
prompt = "Choose your flavor: "
print(flavors)
while (choice := input(prompt)) not in flavors:
  print(f"Sorry, '{choice}' is not a valid option.")
print(f"You chose '{choice}'")