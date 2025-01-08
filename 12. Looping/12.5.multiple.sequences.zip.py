# # multiple.sequences
# people = ["Nick", "Rick", "Roger", "Syd"]
# ages = [23, 24, 23, 21]
# for position in range(len(people)):
#   person = people[position]
#   age = ages[position]
#   print(person, age)

# Output:
# Nick 23
# Rick 24
# Roger 23
# Syd 21

# Una forma más elegeante de hacer lo mismo es:
people = ["Nick", "Rick", "Roger", "Syd"]
ages = [23, 24, 23, 21]
for person, age in zip(people, ages):
  print(person, age)