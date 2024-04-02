import hashlib

def sha256_checksum(file_path):
    """Compute the SHA256 checksum of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

file_paths = [
    "414_Cipher/RootBeerTest365A.pdf",
    "414_Cipher/RootBeerTest365B.pdf",
    "414_Cipher/console1.png",
    "414_Cipher/console2.png"
]

for file_path in file_paths:
    checksum = sha256_checksum(file_path)
    print(f"SHA256 hash of {file_path}: {checksum}")
