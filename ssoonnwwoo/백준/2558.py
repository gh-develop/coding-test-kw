a = int(input())
b = input()
c = list(b)
for i in range(len(c)):
    c[i] = int(c[i])
print(a*c[2])
print(a*c[1])
print(a*c[0])
print(a*int(b))
