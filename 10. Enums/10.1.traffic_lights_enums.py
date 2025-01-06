# Forma común de definir un enumerado en Python
# GREEN = 1
# YELLOW = 2
# RED = 4
# TRAFFIC_LIGHTS = (GREEN, YELLOW, RED)
# # o con un diccionario
# traffic_lights = {"GREEN": 1, "YELLOW": 2, "RED": 4}

from enum import Enum
class TrafficLight(Enum):
    GREEN = 1
    YELLOW = 2
    RED = 4

print(TrafficLight.GREEN.name) # GREEN
print(TrafficLight.GREEN.value) # 1

print(TrafficLight(1)) # TrafficLight.GREEN
print(TrafficLight(4)) # TrafficLight.RED