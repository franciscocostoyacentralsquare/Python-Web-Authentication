### command line interface for login
import cryptography
from cryptography.fernet import Fernet
import client
import json
#intro
print("Hello!\nWelcome to the command line tool for LoginService")
key = b'FjffD4F541-nuZ-HT8-sW-WSNAt7pWQ8cv1sFdHxm60='
#loginFunction
def loginUserName():
    print("Enter user name:")
    username = input()
    return username
def loginPassword():
    print("Enter password:")
    encrypted = input()
    print(f"{username}" + " " + f"{encrypted}")
    return encrypted


username = loginUserName()
encrypted = loginPassword()
f = Fernet(key)
data = json.dumps({"username": username, "encrypted": encrypted})
data = data.encode()
data = f.encrypt(data)
print("attempting login...")
print(data)
client.ts(data)
