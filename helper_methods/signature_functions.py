from ecdsa import SigningKey, VerifyingKey

def create_key() -> tuple[bytes, bytes]:
    priv_k = SigningKey.generate()
    pub_k = priv_k.get_verifying_key()
    return (priv_k.to_pem(), pub_k.to_pem())

def sign(data, private_key) -> str:
    signing_key = SigningKey.from_pem(private_key)
    return signing_key.sign(data.encode('utf-8')).hex()

def check(data, public_key, signature) -> bool:
    verifying_key = VerifyingKey.from_pem(public_key)
    return verifying_key.verify(bytes.fromhex(signature), data)
