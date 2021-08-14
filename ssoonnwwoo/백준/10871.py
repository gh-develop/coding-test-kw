import sys
N, X = map(int, sys.stdin.readline().split())
data =  map(int, sys.stdin.readline().split())
data = list(data)
for i in range(N):
   if data[i] < X :
        print(data[i], end = ' ')