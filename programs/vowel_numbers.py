text = input("Enter a string: ").lower()

vowels = "aeiou"
count = {}

for ch in text:
    if ch in vowels:
        count[ch] = count.get(ch, 0) + 1

print(count)
