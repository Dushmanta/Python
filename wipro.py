# Find the count of duplicate character
fruit = "acclec"
i = 0
for idx in range(len(fruit)):

    if fruit[idx] == 'c':
        i += 1

print(i)
