# scoping.level.2
def outer():
  test = 1 # ámbito externo
  def inner():
    test = 2 # ámbito interno
    print("inner:", test)
  inner()
  print("outer:", test)
test = 0 # ámbito global
outer()
print("global:", test)

# inner: 2
# outer: 1 
# global: 0