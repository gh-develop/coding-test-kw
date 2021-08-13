m = []
x, y = 2, 2
for i in range(10):
    m.append(input().split())

for i in range(10):
    for j in range(10):
        m[i][j] = int(m[i][j])

while True:
    if m[y-1][x]==0:
        m[y-1][x-1] = 9
        x +=1
    elif m[y-1][x]==1:
        if m[y][x-1]==2:
            m[y-1][x-1]=9
            m[y][x-1] = 9
            break
        elif m[y][x-1]==1:
            m[y-1][x-1]=9
            break


        m[y-1][x-1] = 9
        y+=1
    else : 
        m[y-1][x-1] = 9
        m[y-1][x]=9
        break


for i in range(10):
    for j in range(10):
        print(m[i][j],end  = ' ')
    print("")

        