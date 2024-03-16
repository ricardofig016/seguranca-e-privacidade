import os
import random
import string

BASE_FILE_PATH = "random_files/"


def gen_files():
    aes_sizes = [8, 64, 512, 4096, 32768, 262144, 2097152]
    sha_sizes = [8, 64, 512, 4096, 32768, 262144, 2097152]
    rsa_sizes = [2, 4, 8, 16, 32, 64, 128]

    for size in aes_sizes:
        gen_random_file(f"aes_{size}.txt", size)

    for size in sha_sizes:
        gen_random_file(f"sha_{size}.txt", size)

    for size in rsa_sizes:
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
