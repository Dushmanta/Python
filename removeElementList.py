prefixes = ('-', '+')
list = ['-hi', '+helloyou', 'holla', 'byeyou', 'hellooooo']
for word in list[:]:
    if word.startswith(prefixes):
        list.remove(word)
print('list', list)
