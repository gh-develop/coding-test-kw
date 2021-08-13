a, r, n = input().split()
a = int(a)
r = int(r)
n = int(n)
result = a
for i in range(n-1):
    result =result*r  
print(result)