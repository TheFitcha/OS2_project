import hashlib

def generate_hash_sha256(message) -> str:
    hash_obj = hashlib.sha256(message.encode('utf-8'))
    return hash_obj.hexdigest()