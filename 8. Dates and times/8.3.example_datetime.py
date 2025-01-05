from datetime import datetime, date, UTC

now = datetime.now()
print(now)

utcnow = datetime.now(UTC)
print(utcnow)

# Obtener solo la fecha
print(now.date())
print(now.day, now.month, now.year)

# Verificar con la fecha actual
print(now.date() == date.today())

# Obtener solo la hora
print(now.time())
print(now.hour, now.minute, now.second, now.microsecond)

# Representación como cadena legible
print(now.ctime())

# Representación en formato ISO 8601 (YYYY-MM-DDTHH:MM:SS.ssssss)
print(now.isoformat())

# Convertir a una estructura de tiempo
print(now.timetuple())

# Información de la zona horaria
print(now.tzinfo)
print(utcnow.tzinfo)

# Día de la semana (0 = lunes, 6 = domingo)
print(now.weekday())