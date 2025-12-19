import sys
from auth.registration import hash_password, verify_password
from messaging.ecdh import generate_ephemeral_keypair, derive_shared_secret
from messaging.encryption import encrypt_message, decrypt_message

def run_demo():
    print("--- CryptoVault MAT364 Final Project ---")

    # 1. User Registration Simulation
    password = "SuperSecretPassword123!"
    h_key, salt = hash_password(password)
    print(f"[*] User registered. Password hashed with Argon2id.")

    # 2. Secure Messaging Simulation (Alice & Bob)
    print("\n--- Establishing Secure Channel ---")
    a_priv, a_pub = generate_ephemeral_keypair()
    b_priv, b_pub = generate_ephemeral_keypair()

    a_shared = derive_shared_secret(a_priv, b_pub)
    b_shared = derive_shared_secret(b_priv, a_pub)

    assert a_shared == b_shared
    print("[+] Shared Secret established via ECDH.")

    msg = "This is a confidential exam report."
    encrypted = encrypt_message(a_shared, msg)
    print(f"[>] Alice sends encrypted message: {encrypted.hex()[:32]}...")

    decrypted = decrypt_message(b_shared, encrypted)
    print(f"[<] Bob decrypted message: {decrypted}")

if __name__ == "__main__":
    run_demo()