class Person:
  species = "Human"
  
print(Person.species) # Human
Person.alive = True # Agregado dinámicamente
print(Person.alive) # True
man = Person()
print(man.species) # Human
print(Person.alive) # True
Person.alive = False
print(man.alive) # False
man.name = "Darth"
man.surname = "Vader"
print(man.name, man.surname) # Darth Vader