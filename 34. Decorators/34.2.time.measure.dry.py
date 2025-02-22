from time import sleep, time

def f():
  sleep(0.3)
  
def g():
  sleep(0.5)
  
def measure(func):
  t = time()
  func()
  print(func.__name__, "took:", time() - t)
  
measure(f) # f took: 0.3000001907348633
measure(g) # g took: 0.5000002384185791