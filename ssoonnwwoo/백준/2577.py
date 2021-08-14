data = []
cnt = []
for i in range(3):
    data.append(int(input()))

for i in range(10):
    cnt.append(int(0))

mul = data[0]*data[1]*data[2]
mul = str(mul)

for i in range(len(mul)):
    for j in range(10):
        if mul[i] == str(j):
            cnt[j]+=1
for i in range(10):
    print(cnt[i])

