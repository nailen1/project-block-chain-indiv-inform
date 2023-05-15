from Crypto.Cipher import AES
import hashlib


class PersonalInfo:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def encrypt(self, key):
        cipher = AES.new(hashlib.sha256(
            key.encode('utf-8')).digest(), AES.MODE_EAX)
        nonce = cipher.nonce
        name, age, address = map(str, [self.name, self.age, self.address])
        encrypted_name, tag = cipher.encrypt_and_digest(name.encode('utf-8'))
        encrypted_age, tag = cipher.encrypt_and_digest(age.encode('utf-8'))
        encrypted_address, tag = cipher.encrypt_and_digest(
            address.encode('utf-8'))
        return encrypted_name, encrypted_age, encrypted_address, tag, nonce

    @staticmethod
    def decrypt(key, encrypted_name, encrypted_age, encrypted_address, tag, nonce):
        cipher = AES.new(hashlib.sha256(key.encode('utf-8')
                                        ).digest(), AES.MODE_EAX, nonce=nonce)
        name = cipher.decrypt_and_verify(encrypted_name, tag).decode('utf-8')
        age = cipher.decrypt_and_verify(encrypted_age, tag).decode('utf-8')
        address = cipher.decrypt_and_verify(
            encrypted_address, tag).decode('utf-8')
        return PersonalInfo(name, age, address)
