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


if __name__ == "__main__":
    gen_files()

    encryption_times = {}  # in seconds
    decryption_times = {}  # in seconds

    measure_aes()

    ic(encryption_times)
    ic(decryption_times)
