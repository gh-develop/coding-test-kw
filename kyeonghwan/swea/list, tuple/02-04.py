data = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
find = 'aeiou'
result = [i for i in data if i not in find]
print("".join(result))
