# scoping.level.1
def my_function():
  test = 1 # Esto está definido en el ámbito local
  print("my_function:", test)
test = 0 # Esto está definido en el ámbito global
my_function()
print("global:", test)