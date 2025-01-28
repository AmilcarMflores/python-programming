from time import sleep, time

def f():
  sleep(0.3)

def g():
  sleep(0.5)
  
t = time()
f()
print("f took:", time() - t) # f took: 0.3000001907348633 (masomenos 0.3)
t = time()
g()
print("g took:", time() - t) # g took: 0.5000002384185791 (masomenos 0.5)
