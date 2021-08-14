data = []
remainder = []
for i in range(10):
    data.append(int(input()))
    remainder.append(data[i]%42)
remainder = set(remainder)
print(len(remainder))
