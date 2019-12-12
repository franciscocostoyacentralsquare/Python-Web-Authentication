from cryptography.fernet import Fernet

def decryptor(data):
    key = b'FjffD4F541-nuZ-HT8-sW-WSNAt7pWQ8cv1sFdHxm60='
    f = Fernet(key)
    data = f.decrypt(data)
    data = data.decode()
    return data
