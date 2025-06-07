from hashes import salt_gen, password_hasher, binary_to_base64

# Datos del nuevo usuario
username = 'admin'
nombre = 'Administrador'
password = 'n1mbus.C0r3-Admin'

# Paso 1: Generar salt binario
salt = salt_gen()

# Paso 2: Hashear la contraseña con salt
hashed_password = password_hasher(password, salt)

# Paso 3: Convertir salt a base64 para almacenar en la DB
salt_base64 = binary_to_base64(salt)

# Paso 4: Mostrar resultado listo para INSERT
print("\n--- SQL PARA INSERTAR EN POSTGRESQL ---\n")
print(f"""INSERT INTO app_usuario (nombre, username, password, salt)
VALUES (
  '{nombre}',
  '{username}',
  '{hashed_password}',
  '{salt_base64}'
);""")
