message = input("Enter your message: ")
with open('file.txt', 'w') as file:
    file.write(message)
print("Message has been written to 'file.txt'.")