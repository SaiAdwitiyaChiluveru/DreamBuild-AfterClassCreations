char = input("Enter a character: ")
if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
    print(char, "This character is an alphabet.")
else:
    print(char, "This character is not an alphabet.")