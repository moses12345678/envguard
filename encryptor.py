#!/usr/bin/env python3
"""
Author: Moussa Diallo
Version: 1.0.0
License: MIT
Description: Encrypts sensitive key-value pairs using AES encryption and writes the result to .env_encrypted

"""

import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from key_manager import load_key_iv

def encrypt_file(input_file, output_file, key, iv):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            title, value = line.split("=", 1)
            data = value.strip().encode()

            # Pad the data
            padder = padding.PKCS7(128).padder()
            padded = padder.update(data) + padder.finalize()

            # Encrypt
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(padded) + encryptor.finalize()

            # Save as hex for readability
            f_out.write(f"{title} = {ciphertext.hex()}\n")

    print(f"✅ Encrypted values written to {output_file}")

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)

    # Load the key and IV from the key manager
    key, iv = load_key_iv("data/aes.key")

    # Encrypt the sensitive output file
    encrypt_file("data/sensitive_output.txt", "data/.env_encrypted", key, iv)
