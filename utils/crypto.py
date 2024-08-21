from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from typing import Optional


class AliceCrypto:
    def __init__(self) -> None:
        pass

    @staticmethod
    def encrypt(data: bytes, key: bytes, iv: bytes):
        """Encrypt for AES_CBC_256."""
        KEY = key
        IV = iv
        data = pad(data, AES.block_size)
        cipher = AES.new(KEY, AES.MODE_CBC, IV)
        return cipher.encrypt(data)

    @staticmethod
    def decrypt(enc_data: bytes, key: bytes, iv: Optional[bytes] = None):
        """Decrypt for AES_CBC_256."""
        KEY = key
        if iv is not None:
            IV = iv
        else:
            IV = enc_data[:16]
            enc_data = enc_data[16:]
        cipher = AES.new(KEY, AES.MODE_CBC, IV)
        return unpad(cipher.decrypt(enc_data), AES.block_size)
