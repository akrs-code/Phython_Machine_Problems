source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")

try:

    with open(source_file, 'r') as source:
        content = source.read()

    with open(destination_file, 'w') as destination:
        destination.write(content)
    
    print(f"Contents copied from '{source_file}' to '{destination_file}'.")
except FileNotFoundError:
    print("Source file not found.")
