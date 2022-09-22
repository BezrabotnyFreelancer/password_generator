from cryptography.fernet import Fernet


key = Fernet.generate_key()
fernet = Fernet(key)

def encode_password(password: str):
    return fernet.encrypt(password.encode())


def decode_password(password: str, decode_key):
    decoded_fernet = Fernet(decode_key)
    return decoded_fernet.decrypt(password).decode()



