w, h = input().split()
w = int(w)
h = int(h)
m = []
for i in range (w):
    m.append([])
    for j in range(h):
        m[i].append(0)
        m[i][j] = int(m[i][j])

n = int(input())

for i in range(n):
    l, d, x, y = input().split()
    l = int(l)
    d = int(d)
    x = int(x)
    y = int(y)
    if d == 0:
        for j in range(l):
            if m[x-1][j+y-1]==0:
                m[x-1][j+y-1]=1
    else:
        for j in range(l):
            if m[j+x-1][y-1]==0:
                m[j+x-1][y-1]=1



for i in range(w):
    for j in range(h):
        print(m[i][j],end = " ")
    print("")
