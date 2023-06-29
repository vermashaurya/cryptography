def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text)
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return "".join(orig_text)
choice = None
prev_cipher_text = None
while choice != "3":
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        print("use uppercase")
        string = input("Enter the string to encrypt: ")
        keyword = input("Enter the keyword: ")
        key = generateKey(string, keyword)
        cipher_text = cipherText(string, key)
        prev_cipher_text = cipher_text
        print("Ciphertext:", cipher_text)
        print()
    elif choice == "2":
        if prev_cipher_text is None:
            print("No previous ciphertext available for decryption.")
            print()
        else:
            print("1. Decrypt previous ciphertext")
            print("2. Decrypt new ciphertext")
            decrypt_choice = input("Enter your choice (1 or 2): ")
            if decrypt_choice == "1":
                print("This is the text being decrypted:",prev_cipher_text)
                keyword = input("Enter the keyword: ")
                key = generateKey(prev_cipher_text, keyword)
                original_text = originalText(prev_cipher_text, key)
                print("Original/Decrypted Text:", original_text)
                print()
            elif decrypt_choice == "2":
                print("use uppercase")
                cipher_text = input("Enter the ciphertext to decrypt: ")
                keyword = input("Enter the keyword: ")
                key = generateKey(cipher_text, keyword)
                original_text = originalText(cipher_text, key)
                print("Original/Decrypted Text:", original_text)
                print()
            else:
                print("Invalid choice for decryption. Returning to the main menu.")
                print()
    elif choice == "3":
        print("Exiting...")
    else:
        print("Invalid choice! Please select a valid option.")
        print()
