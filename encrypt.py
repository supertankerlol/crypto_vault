from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def encrypt_message(key, plaintext):
    aesgcm = AESGCM(key)
    nonce = os.urandom(12) # GCM standard nonce length
    # Nonce must NEVER be reused with the same key
    ciphertext = aesgcm.encrypt(nonce, plaintext.encode(), None)
    return nonce + ciphertext

def decrypt_message(key, data):
    aesgcm = AESGCM(key)
    nonce = data[:12]
    ciphertext = data[12:]
    return aesgcm.decrypt(nonce, ciphertext, None).decode()