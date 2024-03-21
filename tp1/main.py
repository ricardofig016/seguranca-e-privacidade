import os

from timeit import Timer
from Crypto.Random import get_random_bytes

from files import (
    gen_files,
    AES_SIZES,
    SHA_SIZES,
    RSA_SIZES,
    BASE_FILE_PATH as BASE_RANDOM_FILES_PATH,
)
from aes import encrypt as aes_encrypt, decrypt as aes_decrypt
from rsa import encrypt, decrypt, gen_key_pair
from sha256 import gen_hash

from icecream import ic


def measure_aes():
    for size in AES_SIZES:
        file_path = os.path.join(BASE_RANDOM_FILES_PATH, f"aes_{size}.txt")
        with open(file_path, "r") as file:
            plaintext = file.read()

        # encryption
        timer = Timer(lambda: aes_encrypt(plaintext, get_random_bytes(32)))
        iterations = 100
        time_elapsed = timer.timeit(number=iterations)
        average_time_elapsed = time_elapsed / iterations
        encryption_times[f"aes_{size}"] = average_time_elapsed

        # decryption
        key = get_random_bytes(32)
        encrypted_data = aes_encrypt(plaintext, key)

        timer = Timer(lambda: aes_decrypt(encrypted_data, key))
        iterations = 100
        time_elapsed = timer.timeit(number=iterations)
        average_time_elapsed = time_elapsed / iterations
        decryption_times[f"aes_{size}"] = average_time_elapsed

        # verification
        # print(aes_decrypt(encrypted_data, key).decode("utf-8") == plaintext)

def measure_rsa():
     for size in RSA_SIZES:

        file_path = os.path.join(BASE_RANDOM_FILES_PATH, f"rsa_{size}.txt")
        with open(file_path, "rb") as file:
            plainText = file.read()

        private_key, public_key = gen_key_pair()

        # encryption time
        timer = Timer(lambda: encrypt(public_key, plainText))
        iterations = 100
        time_elapsed = timer.timeit(number=iterations)
        average_time_elapsed = time_elapsed / iterations
        encryption_times[f"rsa_{size}"] = average_time_elapsed

        # decryption time
        cipherText = encrypt(public_key, plainText)
        timer = Timer(lambda: decrypt(private_key, cipherText))
        iterations = 100
        time_elapsed = timer.timeit(number=iterations)
        average_time_elapsed = time_elapsed / iterations
        decryption_times[f"rsa_{size}"] = average_time_elapsed

def measure_sha256():
    for size in SHA_SIZES:

        file_path = os.path.join(BASE_RANDOM_FILES_PATH, f"sha_{size}.txt")
        with open(file_path, "rb") as file:
            plainText = file.read()
        
        # hash time
        timer = Timer(lambda: gen_hash(plainText))
        iterations = 100
        time_elapsed = timer.timeit(number=iterations)
        average_time_elapsed = time_elapsed / iterations
        hash_times[f"sha256_{size}"] = average_time_elapsed



if __name__ == "__main__":
    gen_files()

    encryption_times = {}  # in seconds
    decryption_times = {}  # in seconds
    hash_times = {}        # in seconds

    measure_aes()
    measure_rsa()
    measure_sha256()

    ic(encryption_times)
    ic(decryption_times)
    ic(hash_times)
