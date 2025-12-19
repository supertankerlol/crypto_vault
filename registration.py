from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
import os
import secrets

def hash_password(password: str) -> tuple:
    salt = os.urandom(16)
    # Argon2id is resistant against GPU/ASIC cracking and side-channel attacks
    kdf = Argon2id(
        length=32,
        salt=salt,
        iterations=2,
        memory_cost=65536, # 64MB
        parallelism=4,
    )
    hashed_key = kdf.derive(password.encode())
    return hashed_key, salt

def verify_password(stored_hash, salt, provided_password):
    kdf = Argon2id(
        length=32,
        salt=salt,
        iterations=2,
        memory_cost=65536,
        parallelism=4,
    )
    try:
        kdf.verify(provided_password.encode(), stored_hash)
        return True
    except:
        return False