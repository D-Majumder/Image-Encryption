from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt_image(key, input_file, output_file):
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    key = pad(key.encode('utf-8'), AES.block_size)
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    with open(output_file, 'wb') as f:
        f.write(base64.b64encode(ciphertext))

def decrypt_image(key, input_file, output_file):
    with open(input_file, 'rb') as f:
        ciphertext = base64.b64decode(f.read())

    key = pad(key.encode('utf-8'), AES.block_size)
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    with open(output_file, 'wb') as f:
        f.write(plaintext)

# Example usage
key = 'mysecretpassword'
encrypt_image(key, 'input_image.jpg', 'encrypted_image.enc')
decrypt_image(key, 'encrypted_image.enc', 'decrypted_image.jpg')
