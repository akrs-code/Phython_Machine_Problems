user_input = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for y in user_input:
    if y in vowels:
        count += 1

print("Vowel count", count)

#Abdul-khaliq R. Solaiman