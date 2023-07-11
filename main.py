# Key Scheduling Algorithm
def key_schedular(key):
    j = 0
    s = [i for i in range(256)]  # state vector of 256 bit
    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]  # swap s[i], s[j]
    return s


# Pseudo Random Generator Algorithm
# Generate key stream
def pseudo_random_generator(s):
    i, j = 0, 0
    key_stream = []
    for k in range(0, text_len):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        t = (s[i] + s[j]) % 256
        key_stream.append(s[t])
    return key_stream


# RC4 encryption
def encryption(key, plain_text):
    uni_key = [ord(c) for c in key]  # key convert into unicode
    s = key_schedular(uni_key)
    key_stream = pseudo_random_generator(s)
    ciphertext = []
    for i in range(text_len):
        ciphertext.append(key_stream[i] ^ plain_text[i])  # bitwise XOR
    cipher_text = bytes(ciphertext)
    return cipher_text, s, key_stream  # return cipher_text, s and key_stream


# Decryption from RC4
def decryption(key, cipher_text):
    plaintext, s1, key_stream1 = encryption(key, cipher_text)
    return plaintext, s1, key_stream1  # return plain_text, s1 and key_stream1


if __name__ == '__main__':
    plain_text = "Pasan Narangoda"
    key = "3402"
    text_len = len(plain_text)

    print(f"\nPlaintext: {plain_text}\n")
    print(f"Key: {key}\n")

    print("-----Encryption-----\n")
    # Encryption
    cipher_text, s, key_stream = encryption(key, plain_text.encode())
    print(f"s = {s}\n\nkey stream = {key_stream}\n\nEncrypted text: {cipher_text.hex()}\n")

    print("-----Decryption-----\n")
    # Decryption
    original_text, s1, key_stream1 = decryption(key, cipher_text)
    print(f"s1 = {s}\n\nkey stream = {key_stream1}\n\nDecrypted text: {original_text.decode()}\n")
