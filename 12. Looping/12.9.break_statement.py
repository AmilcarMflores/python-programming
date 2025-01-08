# Any
items = [0, None, 0.0, True, 0, 7]
found = False
for item in items:
  print("scanning item", item)
  if item:
    found = True
    break
if found:
  print("At least one item evaluates to True")
else:
  print("All items evaluate to False")
  
# scanning item 0
# scanning item None
# scanning item 0.0
# scanning item True
# At least one item evaluates to True