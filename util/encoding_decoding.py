from cryptography.fernet import Fernet

def encrypted(password:str):
    f = Fernet(b'FINEHtwMUOxgvyYM9f0vpXcQHYDDZkb3-NkPWTrZN5g=')
    b_password = bytes(password, 'ascii')
    encrypted_password = f.encrypt(b_password)
    return encrypted_password.decode('ascii')


def encrypted(password:str):
    f = Fernet(b'FINEHtwMUOxgvyYM9f0vpXcQHYDDZkb3-NkPWTrZN5g=')
    b_password = bytes(password, 'ascii')
    b_password_decrypt = f.decrypt(b_password)
    return b_password.decode('ascii')

