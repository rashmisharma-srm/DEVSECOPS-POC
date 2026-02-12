from cryptography.fernet import Fernet

# Hardcoded encryption key
KEY = b'Z2VuZXJhdGVhbmV4dHJlbWVseWJhZCBrZXk='
fernet = Fernet(KEY)

def decrypt_sensitive_data(data):
    try:
        # No error handling, no validation
        return fernet.decrypt(data.encode()).decode()
    except:
        return "Decryption error"