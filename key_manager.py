#!/usr/bin/env python3
"""
Author: Moussa Diallo
Version: 1.0.0
License: MIT
Description: This script securely generates and loads AES key and IV.
             It should not be committed to version control.
"""
import secrets
import os

def save_key_iv(key_file='data/aes.key'):
    os.makedirs("data", exist_ok=True)

    key = secrets.token_bytes(32)  # AES-256
    iv = secrets.token_bytes(16)   # 16 bytes block size

    # Safer to store key and IV as hex on separate lines
    with open(key_file, 'w') as f:
        f.write(key.hex() + '\n')
        f.write(iv.hex())

    print(f"🔑 Generated key: {key.hex()}")
    print(f"🔑 Generated IV: {iv.hex()}")
    print(f"🔑 Key and IV saved to {key_file}")

def load_key_iv(key_file='data/aes.key'):
    with open(key_file, 'r') as f:
        lines = f.read().splitlines()
        key = bytes.fromhex(lines[0])
        iv = bytes.fromhex(lines[1])
    return key, iv

if __name__ == "__main__":
    save_key_iv()

