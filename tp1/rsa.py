import os

from timeit import Timer
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

from files import (
    RSA_SIZES,
    BASE_FILE_PATH as BASE_RANDOM_FILES_PATH,
)

# RSA is a public-key algorithm for encrypting and signing messages

# private key for decryption
# public key for encryption

def gen_key_pair(): 
    private_key = rsa.generate_private_key(
        # public_exponent indicates what one mathematical property of the key generation will be
        # unless you have a specific reason to do otherwise, you should always use 65537.
        public_exponent = 65537,
        key_size = 2048
    )

    public_key = private_key.public_key()

    return private_key, public_key

def encrypt(public_key, file_data):
    cipherText = public_key.encrypt(
        file_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=b'')
    )
    return cipherText

def decrypt(private_key, cipherText):
    plainText = private_key.decrypt(
        cipherText,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=b''
        )
    )
    return plainText

