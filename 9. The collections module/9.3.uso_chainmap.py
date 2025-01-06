from collections import ChainMap

default_connection = {'host': 'localhost', 'port': 4567}
connection = {'port': 5678}
conn = ChainMap(connection, default_connection)
print(conn["port"]) # 5678
print(conn["host"]) # localhost

print(conn.maps) # [{'port': 5678}, {'host': 'localhost', 'port': 4567}]

# Eliminamos la información del puerto
del conn["port"]
print(conn.maps) # [{}, {'host': 'localhost', 'port': 4567}]
print(conn["port"]) # 4567

print(dict(conn))  # {'host': 'localhost', 'port': 4567}