import argparse
import os
from extractor import extract_secret_and_database
from key_manager import save_key_iv, load_key_iv
from encryptor import encrypt_file
from decryptor import decrypt_file

def parse_args():
    parser = argparse.ArgumentParser(description="envguard - AES-256 Encryption Tool")
    subparsers = parser.add_subparsers(dest="mode", required=True, help="Operational Modes")

    # Encrypt
    encrypt_parser = subparsers.add_parser("encrypt", help="Encrypts Input File")
    encrypt_parser.add_argument("input_file", help="Input file path")
    encrypt_parser.add_argument("output_file", help="Output file path")
    encrypt_parser.add_argument("--keyfile", default="data/aes.key", help="Key file path")

    # Decrypt
    decrypt_parser = subparsers.add_parser("decrypt", help="Decrypts Input File")
    decrypt_parser.add_argument("input_file", help="Input file path")
    decrypt_parser.add_argument("output_file", help="Output file path")
    decrypt_parser.add_argument("--keyfile", default="data/aes.key", help="Key file path")

    # Extract
    extract_parser = subparsers.add_parser("extract", help="Extract secret")
    extract_parser.add_argument("input_file", help="Input file path")
    extract_parser.add_argument("output_file", help="Output file path")
    extract_parser.add_argument("--keyfile", default="data/aes.key", help="Key file path")

    # Genkey
    genkey_parser = subparsers.add_parser("genkey", help="Generate new AES key and IV")
    genkey_parser.add_argument("--keyfile", default="data/aes.key", help="Key file path")

    return parser.parse_args()
