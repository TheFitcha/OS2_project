import pyaes, pbkdf2, binascii, os, secrets # AES

# AES
# returns AES key and salt
def aes_derive_key(password, salt=None) -> tuple[str, str]:  

    if not salt: # generate random salt if not provided
        salt = os.urandom(16) # random salt (128-bit)

    key = pbkdf2.PBKDF2(password, salt).read(32) # derives 256-bit key via PBKDF2 algorithm
    aes_encryption_key = binascii.hexlify(key) # binary data -> hex

    return (aes_encryption_key, salt)

# returns encrypted data, key and salt
def aes_encrypt(data, password, mode="CTR") -> tuple[str, str, str]: 
    initialization_vector = secrets.randbits(256)
    
    encryption_key, salt = aes_derive_key(password)

    if mode == "CTR":
        aes = pyaes.AESModeOfOperationCTR(encryption_key, pyaes.Counter(initialization_vector))
    
    cipher = aes.encrypt(data)
    return (binascii.hexlify(cipher), encryption_key, salt)

# returns decrpyted data only
def aes_decrypt(cipher, password, salt, init_vector, mode="CTR") -> str:  
    key, salt = aes_derive_key(password, salt)

    if mode == "CTR":
        aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(init_vector))

    decrypted_data = aes.decrypt(cipher)
    return decrypted_data
