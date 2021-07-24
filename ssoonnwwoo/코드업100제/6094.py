a = int(input())
b = input().split()
breaker = False
for i in range(a):
    b[i] = int(b[i])

for i in range(a):
    for j in range(1+i,a):
        
        if b[i]<=b[j]:
            min = b[i]
        else: 
            min = b[j]
            break
        if j==a-1:
            breaker = True
            break
    if breaker == True:
        break
print(min)
