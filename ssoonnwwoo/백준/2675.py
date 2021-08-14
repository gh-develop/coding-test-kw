import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    x, y = input().split()
    x = int(x)
    for i in y:
        print(i*x, end = '')
    print()
