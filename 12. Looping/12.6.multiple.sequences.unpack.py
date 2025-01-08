# Asignamos la tupla a una variable llamada data

people = ["Nick", "Rick", "Roger", "Syd"]
ages = [23, 24, 23, 21]
instruments = ["Drum", "Keyboards", "Bass", "Guitar"]
for data in zip(people, ages, instruments):
  print(data)