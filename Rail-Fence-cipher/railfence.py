def railfence_encrypt(text, key):
    # Create a 2D fence with the dimensions of the text length and key
    fence = [['\n' for _ in range(len(text))] for _ in range(key)]
    dir_down = False
    row, col = 0, 0

    # Fill the fence with the characters of the text
    for i in range(len(text)):
        # Change direction when reaching the top or bottom rail
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        fence[row][col] = text[i]
        col += 1
        row += 1 if dir_down else -1

    # Read characters from the fence and form the cipher text
    result = []
    for i in range(key):
        result.extend([fence[i][j] for j in range(len(text)) if fence[i][j] != '\n'])
    return ''.join(result)

def railfence_decrypt(cipher_text, key):
    # Create a 2D fence with the dimensions of the cipher text length and key
    fence = [['\n' for _ in range(len(cipher_text))] for _ in range(key)]
    dir_down = None
    row, col = 0, 0

    # Mark the positions in the fence where the characters of the cipher text will be placed
    for i in range(len(cipher_text)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        fence[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1

    # Place the characters of the cipher text in the marked positions in the fence
    index = 0
    for i in range(key):
        for j in range(len(cipher_text)):
            if fence[i][j] == '*' and index < len(cipher_text):
                fence[i][j] = cipher_text[index]
                index += 1

    # Read characters from the fence in a zigzag pattern to retrieve the plain text
    result = []
    row, col = 0, 0
    for _ in range(len(cipher_text)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        if fence[row][col] != '*':
            result.append(fence[row][col])
        col += 1
        row += 1 if dir_down else -1

    return ''.join(result)

def main():
    while True:
        print("Rail Fence Cipher")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            plain_text = input("Enter the plain text: ")
            rails = int(input("Enter the number of rails: "))
            cipher_text = railfence_encrypt(plain_text, rails)
            print("Cipher Text:", cipher_text)
            print()

        elif choice == '2':
            cipher_text = input("Enter the cipher text: ")
            rails = int(input("Enter the number of rails: "))
            plain_text = railfence_decrypt(cipher_text, rails)
            print("Decrypted Text:", plain_text)
            print()

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")
            print()

if __name__ == "__main__":
    main()
