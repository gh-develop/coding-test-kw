def d(n):
    n = n + sum(map(int,str(n)))
    return n

data = []

for i in range(1,10001):
    data.append(d(i))

for i in range(1,10001):
    if i not in data:
        print(i)
