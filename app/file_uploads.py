import os

UPLOAD_DIR = "uploads/"

def save_user_file(file):
    # Insecure: no file extension check (RCE possible)
    file_path = UPLOAD_DIR + file.filename
    file.save(file_path)
    return f"File saved to {file_path}"