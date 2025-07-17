import argparse
import os
from extractor import extract_secret_and_database
from key_manager import save_key_iv, load_key_iv
from encryptor import encrypt_file
from decryptor import decrypt_file

def parse_args():
    parser = argparse.ArgumentParser(description="envguard") #Application Description
    
    parser.add_argument("mode", choices=["encrypt", "decrypt", "extract", "genkey"], help="Operation to perform")
    # Argument for Input/Output file path for encryption and decryption 
    parser.add_argument("input_file", help="Input file path")
    # Argument for Input/Output file path for encryption and decryption 
    parser.add_argument("output_file", help="Output file path")
    # Optional argument for keyfile, defaulted to data/aes.key 
    parser.add_argument("--keyfile", default="data/aes.key", help="Key file path")

    args = parser.parse_args()

    if args.mode == "genkey":
            save_key_iv(args.keyfile)
            return

    if not os.path.exists(args.keyfile):
        print(f"Key file {args.keyfile} does not exist, generate a key first")
        return

    
    key, iv = load_key_iv(args.keyfile)

    if args.mode == "extract": #Extract secret and database
        extract_secret_and_database(args.input_file, args.output_file)
    elif args.mode == "encrypt": #Encrypt the input file using key, iv 
        encrypt_file(args.input_file, args.output_file, key, iv)
    elif args.mode == "decrypt": #Decrypt the input file using key, iv 
        decrypt_file(args.input_file, args.output_file, key, iv)


parse_args()






