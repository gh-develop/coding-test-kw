a = int(input())
b = input().split()

for i in range(a):#chr-->int
    b[i]=int(b[i])

count=[]
for i in range(24):
    count.append(0)
for i in range(a):
    count[b[i]]+=1
for i in range(1,24):
    print(count[i],end = " ")