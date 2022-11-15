import pyaes, pbkdf2, binascii, os, secrets # AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES

# # AES
# # returns AES key and salt
# def aes_derive_key(password, salt=None, generateSalt=False) -> str: 

#     # if not salt and generateSalt: # generate random salt if not provided
#     #     salt = os.urandom(16) # random salt (128-bit)
#     #     key = pbkdf2.PBKDF2(password, salt).read(32) # derives 256-bit key via PBKDF2 algorithm
#     # else:
#     #     key = pbkdf2.PBKDF2(password, '').read(32)

#     salt = os.urandom(16) # random salt (128-bit)
#     key = pbkdf2.PBKDF2(password, salt).read(32) # derives 256-bit key via PBKDF2 algorithm
    
#     aes_encryption_key = binascii.hexlify(key) # binary data -> hex

#     return aes_encryption_key

# # returns encrypted data, key and salt
# def aes_encrypt(data, key, mode="CTR") -> str: 
#     # initialization_vector = secrets.randbits(256)
    
#     #encryption_key, salt = aes_derive_key(password)

#     encryption_key = key.encode('utf-8')
#     if mode == "CTR":
#         aes = pyaes.AESModeOfOperationCTR(encryption_key)
    
#     cipher = aes.encrypt(data)
#     return binascii.hexlify(cipher)

# # returns decrpyted data only
# def aes_decrypt(cipher, key, salt=None, init_vector=None, mode="CTR") -> str:  
#     if mode == "CTR":
#         aes = pyaes.AESModeOfOperationCTR(key)

#     decrypted_data = aes.decrypt(cipher)
#     return decrypted_data

def aes_derive_key() -> str:
    return get_random_bytes(16).decode('utf-8')

def aes_encrypt(data, key, mode="CTR") -> tuple:
    cipher = AES.new(key, AES.MODE_CTR)
    encrypted_bytes = cipher.encrypt(data)
    # nonce?
