from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import unpad


def encrypt(plaintext, key):
    iv = get_random_bytes(AES.block_size)

    cipher = AES.new(key, AES.MODE_CBC, iv)

    pad = lambda s: s + (AES.block_size - len(s) % AES.block_size) * chr(
        AES.block_size - len(s) % AES.block_size
    )
    plaintext = pad(plaintext).encode("utf-8")

    ciphertext = cipher.encrypt(plaintext)

    return iv + ciphertext


def decrypt(ciphertext, key):
    iv = ciphertext[: AES.block_size]
    ciphertext = ciphertext[AES.block_size :]

    cipher = AES.new(key, AES.MODE_CBC, iv)

    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    return plaintext
