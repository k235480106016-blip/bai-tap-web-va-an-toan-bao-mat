import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def demo_aes():
    key = os.urandom(16)
    plaintext = "Bài tập môn An toàn và bảo mật thông tin".encode('utf-8')

    print("=== DỮ LIỆU BAN ĐẦU ===")
    print("Plaintext:", plaintext.decode('utf-8'))

    # Mã hóa CBC
    iv = os.urandom(16)
    cipher_encrypt = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(plaintext, AES.block_size)
    ciphertext = cipher_encrypt.encrypt(padded_data)

    print("\n=== MÃ HÓA ===")
    print("Ciphertext (Hex):", ciphertext.hex())

    # Giải mã CBC
    cipher_decrypt = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded = cipher_decrypt.decrypt(ciphertext)
    decrypted_data = unpad(decrypted_padded, AES.block_size)

    print("\n=== GIẢI MÃ ===")
    print("Decrypted text:", decrypted_data.decode('utf-8'))

if __name__ == "__main__":
    demo_aes()