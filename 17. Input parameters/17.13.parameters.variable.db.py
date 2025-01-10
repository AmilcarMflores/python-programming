def connect(**options):
  conn_params = {
    "hots": options.get("host", "127.0.0.1"),
    "port": options.get("port", 5432),
    "user": options.get("user", ""),
    "pwd": options.get("pwd", ""),
  }
  print(conn_params)
  # Luego nos conectamos a la base de datos
  #db.connect(**conn_params)
connect() # Conexión por defecto
connect(host="127.0.0.42", port=5433) # Cambiamos el host y el puerto
connect(port=5431, user="fab", pwd="gandalf") # Cambiamos el puerto, usuario y contraseña