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
from aes import aes_encrypt
from icecream import ic


if __name__ == "__main__":
    gen_files()

    encryption_times = {}  # in seconds
    decryption_times = {}  # in seconds

    # AES
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
        # to implement...

    ic(encryption_times)
