user_input = input("Enter the file name: ")
file = open(user_input, 'r')
content = file.read()
print(content)
file.close()
