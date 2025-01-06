greet_old = "Hello %s!"
print(greet_old % "world") # Hello world!

# Otra forma:
greet_positional = "Hello {}!"
print(greet_positional.format("world")) # Hello world!

greet_positional = "Hello {} {}!"
print(greet_positional.format("world", "again")) # Hello world again!

greet_positional_idx = "This is {0}! {1} loves {0}!"
print(greet_positional_idx.format("Python", "Everyone")) # This is Python! Everyone loves Python!

print(greet_positional_idx.format("Java", "Nobody")) # This is Java! Nobody loves Java!

keyword = "Hello, my name is {name} {last_name}"
print(keyword.format(name="Fabrizio", last_name="Romano")) # Hello, my name is Fabrizio Romano