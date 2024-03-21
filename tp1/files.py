import os
import random
import string

BASE_FILE_PATH = "random_files/"

AES_SIZES = [8, 64, 512, 4096, 32768, 262144, 2097152]
SHA_SIZES = [8, 64, 512, 4096, 32768, 262144, 2097152]
RSA_SIZES = [2, 4, 8, 16, 32, 64, 128]


def gen_files():
    for size in AES_SIZES:
        gen_random_file(f"aes_{size}.txt", size)

    for size in SHA_SIZES:
        gen_random_file(f"sha_{size}.txt", size)

    for size in RSA_SIZES:
        gen_random_file(f"rsa_{size}.txt", size)


def gen_random_file(filename: str, size: int) -> None:
    content = "".join(random.choices(string.ascii_letters + string.digits, k=size))

    if not os.path.exists(BASE_FILE_PATH):
        os.makedirs(BASE_FILE_PATH)

    path = os.path.join(BASE_FILE_PATH, filename)
    with open(path, "w") as file:
        file.write(content)


def get_file_size(filename):
    path = os.path.join(BASE_FILE_PATH, filename)
    if os.path.exists(path):
        file_size = os.path.getsize(path)
        return file_size
    return None
