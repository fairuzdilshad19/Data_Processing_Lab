text = input("Enter a word or sentence: ")

vowels="aeiouAEIOU"
vowel_count=0
space_count=0

for character in text:
    if character in vowels:
        vowel_count=vowel_count+1

    if character== " ":
        space_count=space_count+1

print("Number of characters:", len(text))
print("Number of vowels:", vowel_count)
print("Number of spaces:", space_count)