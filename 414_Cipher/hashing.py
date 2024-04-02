import hashlib

def sha1_checksum(file_path):
    """Compute the SHA1 checksum of a file."""
    sha1 = hashlib.sha1()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha1.update(chunk)
    return sha1.hexdigest()

file_paths = ["414_Cipher/RootBeerTest365A.pdf", "414_Cipher/RootBeerTest365B.pdf"]

for file_path in file_paths:
    checksum = sha1_checksum(file_path)
    print(f"SHA1 hash of {file_path}: {checksum}")

