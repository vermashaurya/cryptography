def shaurya_railfence(text, key):
    fence = [['\n' for _ in range(len(text))] for _ in range(key)]
    dir_down = False
    row, col = 0, 0
    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        fence[row][col] = text[i]
        col += 1
        row += 1 if dir_down else -1
    result = []
    for i in range(key):
        result.extend([fence[i][j] for j in range(len(text)) if fence[i][j] != '\n'])
    return ''.join(result)
def main():
    num_strings = int(input("Enter the number of strings: "))
    for _ in range(num_strings):
        plain_text = input("Enter the plain text: ")
        rails = int(input("Enter the number of rails: "))
        cipher_text = shaurya_railfence(plain_text, rails)
        print("Cipher Text:", cipher_text)
        print()
if __name__ == "__main__":
    main()
