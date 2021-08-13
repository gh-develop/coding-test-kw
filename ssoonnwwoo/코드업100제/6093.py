a = int(input())
b = input().split()

for i in range(a):
    b[i] = int(b[i])
for i in range(1,a+1):
    print(b[-i],end = ' ')