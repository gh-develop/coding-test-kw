words = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'

word_list = [word for word in words if word != 'a' and word != 'e' and word != 'i' and word != 'o' and word != 'u']

print("".join(word_list))
