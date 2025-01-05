import time

print(time.ctime()) # Nos proporciona la fecha y hora actual en formato de cadena
print(time.daylight) # Nos proporciona la diferencia en segundos entre la hora local y la hora UTC
print(time.gmtime()) # Nos proporciona la fecha y hora actual en estructura time.struct_time
print(time.gmtime(0))
print(time.localtime()) # Nos proporciona la fecha y hora actual en estructura time.struct_time
print(time.time()) # Nos proporciona la fecha y hora actual en segundos desde el 1 de enero de 1970