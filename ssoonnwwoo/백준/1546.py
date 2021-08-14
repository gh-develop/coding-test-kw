import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
max = max(data)
newdata=[]
for i in data:
    newdata.append(i/max*100)
sum = 0
for i in newdata:
    sum += i
print(sum/n)