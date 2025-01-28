from time import sleep, time

def f(sleep_time=0.1):
  sleep(sleep_time)

def measure(func):
  def wrapper(*args, **kwargs):
    t = time()
    func(*args, **kwargs)
    print(func.__name__, "took:", time() - t)
  return wrapper

f = measure(f) # Punto de decoración
f(0.2) # f took: 0.20000004768371582 (masomenos 0.2)
f(sleep_time=0.3) # f took: 0.3000001907348633 (masomenos 0.3)
print(f.__name__) # wrapper <- ouch! (no es f)