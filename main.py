from extractor import extract_secret_and_database
from key_manager import save_key_iv, load_key_iv
from encryptor import encrypt_file
from decryptor import decrypt_file

extract_secret_and_database("settings.py", '.env')
save_key_iv()
key, iv = load_key_iv()
encrypt_file("data/sensitive_output.txt", "data/.env_encrypted", key, iv)
decrypt_file("data/.env_encrypted", "data/.env_decrypted", key, iv)