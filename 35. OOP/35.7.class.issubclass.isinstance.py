from class_inheritance import Car, RaceCar, F1Car

car = Car()
racecar = RaceCar()
f1car = F1Car()
cars = [(car, "car"), (racecar, "racecar"), (f1car, "f1car")]
car_classes = [Car, RaceCar, F1Car]
for car, car_name in cars:
  for class_ in car_classes:
    belongs = isinstance(car, class_)
    msg = "es un" if belongs else "no es un"
    print(car_name, msg, class_.__name__)

"""
Output:
car es un Car
car no es un RaceCar
car no es un F1Car
racecar es un Car
racecar es un RaceCar
racecar no es un F1Car
f1car es un Car
f1car es un RaceCar
f1car es un F1Car
"""

