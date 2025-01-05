from datetime import date, datetime, timedelta, timezone, UTC
import time
import calendar as cal
from zoneinfo import ZoneInfo

# Nos proporciona la fecha actual
today = date.today() 

# Nos proporciona la fecha y hora actual
current_datetime = datetime.now()

# Métodos útiles
print(today.isoformat())  # Fecha en formato ISO 8601
print(today.weekday())    # Día de la semana como entero de 0 a 6 (lunes a domingo)
print(cal.day_name[today.weekday()]) # Nombre del día en inglés
print((today.day, today.month, today.year)) # Tupla como tupla
print(today.timetuple()) # Fecha en estructura time.struct_time
