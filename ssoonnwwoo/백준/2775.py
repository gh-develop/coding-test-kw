T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    a = [j for j in range(1,n+1)]
    for floor in range(k):
        for room in range(n-1):
            a[room+1]+=a[room]
    print(a[-1])
   