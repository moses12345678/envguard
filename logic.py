import os
from key_manager import save_key_iv, load_key_iv
from extractor import extract_secret_and_database
from encryptor import encrypt_file
from decryptor import decrypt_file

def operation_logic(args):
    if args.mode == "genkey":
        save_key_iv(args.keyfile)
        return

    if not os.path.exists(args.keyfile):
        print(f" Key file {args.keyfile} does not exist. Please generate one first.")
        return

    key, iv = load_key_iv(args.keyfile)

    if args.mode == "extract":
        extract_secret_and_database(args.input_file, args.output_file)
    elif args.mode == "encrypt":
        encrypt_file(args.input_file, args.output_file, key, iv)
    elif args.mode == "decrypt":
        decrypt_file(args.input_file, args.output_file, key, iv)
