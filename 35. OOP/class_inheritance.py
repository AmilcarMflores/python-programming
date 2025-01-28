# Es una clase simple con dos métodos
class Engine:
  def start(self):
    pass
  def stop(self):
    pass

# Heredan de la clase Engine
class ElectricEngine(Engine): # Is-A Engine
  pass
class V8Engine(Engine): # Is-A Engine
  pass

# Luego declararemos algunos tipos de automóviles que utilizarán esos motores:

# Car es una clase base tanto para RaceCar como para CityCar.
class Car:
  engine_cls = Engine
  def __init__(self):
    self.engine = self.engine_cls() # Has-A Engine
  def start(self):
    print(
      f"Starting {self.engine.__class__.__name__} for "
      f"{self.__class__.__name__}... Wroom, wroom!"
    )
    self.engine.start()
  def stop(self):
    self.engine.stop()

# RaceCar también es una clase base para F1Car.
class RaceCar(Car): # Is-A Car
  engine_cls = V8Engine

class CityCar(Car): # Is-A Car
  engine_cls = ElectricEngine

# F1Car hereda de RaceCar y, por lo tanto, también de Car.
class F1Car(RaceCar): # Is-A RaceCar and also Is-A Car
  pass 
car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()
cars = [car, racecar, citycar, f1car]
for car in cars:
  car.start()