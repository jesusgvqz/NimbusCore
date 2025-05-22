import os
import hashlib

def salt_gen():
    """Genera un salt aleatorio de 16 bytes"""
    return os.urandom(16)

def password_hasher(password, salt):
    """Genera un hash SHA-512 de la contraseña con un salt"""
    password_combined = password.encode('utf-8') + salt
    hasher = hashlib.sha512()
    hasher.update(password_combined)
    return hasher.hexdigest()

def password_auth(password, hash_almacenado, salt_almacenado):
    """Verifica si la contraseña es válida comparando el hash calculado con el hash almacenado"""
    password_combined = password.encode('utf-8') + salt_almacenado
    hasher = hashlib.sha512()
    hasher.update(password_combined)
    return hash_almacenado == hasher.hexdigest()
