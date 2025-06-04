def caesar_encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def get_user_input():
    print("Caesar Cipher Program")
    print("=" * 20)
    
    while True:
        choice = input("\nChoose operation:\n1. Encrypt\n2. Decrypt\n3. Exit\nEnter choice (1-3): ").strip()
        
        if choice == '3':
            print("Goodbye!")
            break
        elif choice not in ['1', '2']:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue
        
        message = input("Enter your message: ")

        if message.isdigit():
            print("Only Alphabet are vaild")
            return
        
        while True:
            try:
                shift = int(input("Enter shift value (0-25): "))
                if 0 <= shift <= 25:
                    break
                else:
                    print("Shift value must be between 0 and 25.")
            except ValueError:
                print("Please enter a valid integer.")
        
        if choice == '1':
            encrypted = caesar_encrypt(message, shift)
            print(f"\nOriginal message: {message}")
            print(f"Encrypted message: {encrypted}")
        else:
            decrypted = caesar_decrypt(message, shift)
            print(f"\nEncrypted message: {message}")
            print(f"Decrypted message: {decrypted}")


def demonstrate_cipher():
    print("\nDemonstration:")
    print("-" * 15)
    
    original = "Hello World!"
    shift = 3
    encrypted = caesar_encrypt(original, shift)
    decrypted = caesar_decrypt(encrypted, shift)
    
    print(f"Original: {original}")
    print(f"Encrypted (shift {shift}): {encrypted}")
    print(f"Decrypted: {decrypted}")
    
    original2 = "Python Programming"
    shift2 = 13
    encrypted2 = caesar_encrypt(original2, shift2)
    decrypted2 = caesar_decrypt(encrypted2, shift2)
    
    print(f"\nOriginal: {original2}")
    print(f"Encrypted (shift {shift2}): {encrypted2}")
    print(f"Decrypted: {decrypted2}")


if __name__ == "__main__":
    demonstrate_cipher()
    get_user_input()
