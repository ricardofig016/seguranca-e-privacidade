from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def aes_encrypt(plaintext, key):
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes for AES-256.")

    iv = get_random_bytes(AES.block_size)

    cipher = AES.new(key, AES.MODE_CBC, iv)

    pad = lambda s: s + (AES.block_size - len(s) % AES.block_size) * chr(
        AES.block_size - len(s) % AES.block_size
    )
    plaintext = pad(plaintext).encode("utf-8")

    ciphertext = cipher.encrypt(plaintext)

    return iv + ciphertext
