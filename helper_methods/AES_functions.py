from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

I_VECTOR = b"a"*16

def aes_derive_key() -> str:
    return b64encode(get_random_bytes(16)).decode('utf-8')

def encrypt_data(data, key, mode="CBC") -> str:
    cipher = AES.new(b64decode(key), AES.MODE_CBC, iv=I_VECTOR)
    cipher_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    cipher_decoded = b64encode(cipher_bytes).decode('utf-8')
    return cipher_decoded

def decrypt_data(data, key, mode="CBC") -> str:
    cipher = AES.new(b64decode(key), AES.MODE_CBC, iv=I_VECTOR)
    decrypted = unpad(cipher.decrypt(b64decode(data)), AES.block_size)
    return decrypted
