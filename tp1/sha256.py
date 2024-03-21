# A cryptographic hash function takes an arbitrary block of data and calculates a fixed-size bit string 
# (a digest), such that different data results (with a high probability) in different digests

from cryptography.hazmat.primitives import hashes

def gen_hash(plainText): 
    digest = hashes.Hash(hashes.SHA256())
    digest.update(plainText)
    return digest.finalize()