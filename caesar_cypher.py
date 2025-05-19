def caesar_cipher_encrypt(location, shift=3):
    encrypted = ""
    for char in location:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around the alphabet
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char  # Non-alphabetic characters are not changed
    return encrypted

# Application
location = "Sokcho"
encrypted_location = caesar_cipher_encrypt(location)
print("Encrypted location:", encrypted_location)
