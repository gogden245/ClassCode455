import hashlib

def md5_checksum(file_path):
    """Compute the MD5 checksum of a file."""
    md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            md5.update(chunk)
    return md5.hexdigest()

file_paths = ["414_Cipher/console1.png", "414_Cipher/console2.png"]

for file_path in file_paths:
    checksum = md5_checksum(file_path)
    print(f"MD5 hash of {file_path}: {checksum}")
