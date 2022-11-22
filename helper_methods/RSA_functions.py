from Cryptodome.PublicKey import RSA # RSA
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_OAEP
import binascii

def generate_rsa_keys(passphrase=None) -> tuple[str, str]:  
    key = RSA.generate(2048)
    return (key.export_key(), key.public_key().export_key())

def encrypt_data(data, key) -> str:
    key_pair = RSA.import_key(key)
    rsa_encryptor = PKCS1_OAEP.new(key_pair) 
    encrypted = rsa_encryptor.encrypt(data.encode('utf-8'))
    return binascii.hexlify(encrypted).decode()

def decrypt_data(data, key) -> str:
    key_pair = RSA.import_key(key)
    rsa_decryptor = PKCS1_OAEP.new(key_pair)
    decrypted = rsa_decryptor.decrypt(binascii.unhexlify(data))
    return decrypted
