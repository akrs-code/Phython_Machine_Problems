favorite_colors = {
    "Alice": "Blue",
    "Bob": "Green",
    "Charlie":"Red"
}
print("Names in the dictionary: ",', '.join(favorite_colors.keys()))

print(favorite_colors["Charlie"])

'''
name = input("Enter a name to find their favorite color: ")


if name in favorite_colors:
    print(f"{name}'s favorite color is {favorite_colors[name]}.")
else:
    print("Name not found in the dictionary")'''