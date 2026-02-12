import hashlib

def insecure_hash(password: str):
    # Weak hashing algorithm
    return hashlib.md5(password.encode()).hexdigest()