#!/usr/bin/env python3
"""
Author: Moussa Diallo
Version: 1.0.0
License: MIT
Description: Decrypts AES-encrypted values from .env_encrypted and writes to .env_decrypted

"""

import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from key_manager import load_key_iv

def decrypt_file(input_file, output_file, key, iv):
    """
    Decrypts the contents of an encrypted file and writes the decrypted data to an output file.
    :param input_file: The file containing encrypted data.
    :param output_file: The file where decrypted data will be saved.
    :param key: The AES key used for decryption.
    :param iv: The initialization vector used for decryption.
    """
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            title, hex_cipher = line.split("=", 1)
            ciphertext = bytes.fromhex(hex_cipher.strip())

            # Decrypt
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            padded = decryptor.update(ciphertext) + decryptor.finalize()

            # Unpad
            unpadder = padding.PKCS7(128).unpadder()
            data = unpadder.update(padded) + unpadder.finalize()

            f_out.write(f"{title.strip()} = {data.decode()}\n")

    print(f"✅ Decrypted values written to {output_file}")

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)

    # Load the key and IV from the key manager
    key, iv = load_key_iv("data/aes.key")

    # Decrypt the encrypted file into the output file
    decrypt_file("data/.env_encrypted", "data/.env_decrypted", key, iv)
