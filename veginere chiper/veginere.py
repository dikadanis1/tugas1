def vigenere_cipher(text, key, mode='encrypt'):
    result = []
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('a')
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            if mode == 'encrypt':
                shifted_char = chr((ord(char) - base + shift) % 26 + base)
            else:
                shifted_char = chr((ord(char) - base - shift) % 26 + base)

            result.append(shifted_char)
        else:
            result.append(char)
    return ''.join(result)

def main():
    text = input("Masukkan teks yang ingin dienkripsi/didekripsi: ")
    key = input("Masukkan kunci: ")
    mode = input("Pilih mode ('encrypt' atau 'decrypt'): ").lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Mode tidak valid. Harap pilih 'encrypt' atau 'decrypt'.")
        return

    result = vigenere_cipher(text, key, mode)
    print(f"Hasil {mode}ion: {result}")