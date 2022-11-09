from Cryptodome.PublicKey import RSA # RSA
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_OAEP
import binascii

# RSA
# returns private and public 2048-bit RSA key -> ONLY FOR FILEWRITING
def generate_rsa_keys(passphrase=None) -> tuple[str, str]:  
    key = RSA.generate(2048)
    return (key.export_key().decode('ascii'), key.public_key().export_key().decode('ascii'))

# returns encrypted data
def encrypt_data(data, key=None) -> str:
    if not key:
        key_pair = RSA.generate(2048) # if there's no key, generate one
    else:
        key_pair = RSA.import_key(key)  # this 'key' includes private key (?)

    rsa_encryptor = PKCS1_OAEP.new(key_pair)  # RsaKey as argument
    encrypted = rsa_encryptor.encrypt(data)
    return binascii.hexlify(encrypted)

# returns decrypted data
def decrypt_data(data, key) -> str:
    key_pair = RSA.import_key(key)
    rsa_decryptor = PKCS1_OAEP.new(key_pair)
    decrypted = rsa_decryptor.decrypt(data)
    return decrypted
