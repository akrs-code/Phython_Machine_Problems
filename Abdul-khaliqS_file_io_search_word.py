filename = input("Enter the filename: ")
word_to_search = input("Enter the word to search for: ").lower()

try:
    with open(filename, 'r') as file:
        content = file.read().lower()

    word_count = content.count(word_to_search)

    print(f"The word '{word_to_search}' appears {word_count} time(s) in the file.")
except FileNotFoundError:
    print(f"File '{filename}' not found.")