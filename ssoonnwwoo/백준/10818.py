import sys
n = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))

min = data[0]
max = data[0]

for i in data[1:]:
    if min >= i:
        min = i
for i in data[1:]:
    if max<= i:
        max = i
print(min, max)