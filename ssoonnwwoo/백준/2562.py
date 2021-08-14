import sys

data = []

for i in range(9):
    data.append(int(sys.stdin.readline()))
max = data[0]
for i in data[1:]:
    if max <= i:
        max = i
print(max)
for i in range(9):
    if data[i] == max:
        print(i+1)
