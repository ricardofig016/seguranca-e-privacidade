from files import gen_files, get_file_size

if __name__ == "__main__":
    gen_files()
    """
    # verification of the file sizes
    for filename in ["aes_8.txt", "aes_2097152.txt"]:
        print(get_file_size(filename))
    """
