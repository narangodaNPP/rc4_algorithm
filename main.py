# Key Scheduling Algorithm
def key_schedular(key):
    j = 0
    s = [i for i in range(256)]  # initial state vector of 256 bit [0-255]
    print(f"s vector = {s}\n")
    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]  # swap s[i], s[j]
    print(f"s = {s}\n")
    return s


# Pseudo Random Generator Algorithm
# Generate key stream
def pseudo_random_generator(s):
    i, j = 0, 0
    key_stream = []
    for k in range(0, text_len):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]  # swap s[i] and s[j]
        print(f"{k} : {s}")
        t = (s[i] + s[j]) % 256
        key_stream.append(s[t])  # generate key stream
    return key_stream


# RC4 encryption
def encryption(key, plain_text):
    uni_key = [ord(c) for c in key]  # key convert into unicode
    s = key_schedular(uni_key)  # state vector
    key_stream = pseudo_random_generator(s)  # key stream
    print(f"\nkey stream = {key_stream}\n")  # print key stream
    ciphertext = []
    for i in range(text_len):
        ciphertext.append(key_stream[i] ^ plain_text[i])  # bitwise XOR
    cipher_text = bytes(ciphertext)
    return cipher_text  # return cipher_text


# Decryption from RC4
def decryption(key, cipher_text):
    plaintext = encryption(key, cipher_text)
    return plaintext  # return plain_text


if __name__ == '__main__':
    plain_text = "Narangoda N.P.P"  # name
    key = "3402"  # EG/2018/3402
    text_len = len(plain_text)  # name length

    print(f"\nPlaintext: {plain_text}\n")
    print(f"Key: {key}\n")

    print("-----Encryption-----\n")
    # Encryption
    cipher_text = encryption(key, plain_text.encode())
    print(f"Encrypted text: {cipher_text.hex()}\n")  # hexadecimal cipher text

    print("-----Decryption-----\n")
    # Decryption
    original_text = decryption(key, cipher_text)
    print(f"Decrypted text: {original_text.decode()}\n")  # decrypted output
