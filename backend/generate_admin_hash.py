# generate_admin_hash.py
from app.hashes import salt_gen, password_hasher, binary_to_base64

# Datos del admin
username = "admin"
password_plano = "plaintext"
nombre = "Administrador"

# Generar salt y hash
salt = salt_gen()
salt_base64 = binary_to_base64(salt)
password_hash = password_hasher(password_plano, salt)

# Mostrar resultado para copiar
print("INSERT INTO app_usuario (nombre, username, password, salt)")
print(f"VALUES ('{nombre}', '{username}', '{password_hash}', '{salt_base64}');")