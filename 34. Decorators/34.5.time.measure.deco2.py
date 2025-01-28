from time import sleep, time
from functools import wraps
def measure(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    t = time()
    func(*args, **kwargs)
    print(func.__name__, "took:", time() - t)
  return wrapper
@measure
def f(sleep_time=0.1):
  """Yo soy un gato, y me gusta dormir!!!"""
  sleep(sleep_time)
f(sleep_time=0.3) # f took: 0.3000001907348633 (masomenos 0.3)
print(f.__name__) # f
print(f.__doc__) # Yo soy un gato, y me gusta dormir!!!