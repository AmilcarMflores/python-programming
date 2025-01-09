# scoping.level.2.global.py
def outer():
  test = 1 # outer scope
  def inner():
    global test
    test = 2 # nearest enclosing scope (outer)
    print("inner:", test)
  inner()
  print("outer:", test)
test = 0 # global scope
outer()
print("global:", test)

# inner: 2
# outer: 1 
# global: 2