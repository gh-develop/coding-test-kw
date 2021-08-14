import sys
n = int(sys.stdin.readline())
for i in range(n):
    cnt = 0
    data = list(map(int, sys.stdin.readline().split()))
    average = sum(data[1:])/data[0]
    for j in data[1:]:
        if j > average:
            cnt += 1
    result = cnt/data[0]*100
    print("%.3f%%" %result)
