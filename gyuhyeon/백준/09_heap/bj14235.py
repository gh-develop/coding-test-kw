import sys
import heapq
sys.stdin = open('bj14235_in.txt', 'r')

charge = []
n = int(input())

for i in range(n):
    data = list(map(int, input().split()))

    if len(data) == 1:
        if len(charge) == 0:
            print(-1)
        else:
            print(-heapq.heappop(charge))
    else:

        iteration = data[0]
        for j in range(1,iteration+1):
            heapq.heappush(charge, -data[j])

