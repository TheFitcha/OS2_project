from ecdsa import SigningKey, VerifyingKey
import binascii

def create_key() -> tuple[bytes, bytes]:
    priv_k = SigningKey.generate()
    pub_k = priv_k.get_verifying_key()
    return (priv_k.to_pem(), pub_k.to_pem())

def sign(data, private_key) -> str:
    signing_key = SigningKey.from_pem(private_key)
    signed = signing_key.sign(data.encode('utf-8'))
    return binascii.hexlify(signed).decode()

def check(data, public_key, signature) -> bool:
    verifying_key = VerifyingKey.from_pem(public_key)
    try:
        return verifying_key.verify(binascii.unhexlify(signature), data.encode('utf-8'))
    except Exception:
        return False
