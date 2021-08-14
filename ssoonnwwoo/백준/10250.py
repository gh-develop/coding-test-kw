import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    share = N // H + 1
    remain = N % H
    if remain == 0 :     
        share = N // H
        remain = H
    print(remain*100 + share)    
