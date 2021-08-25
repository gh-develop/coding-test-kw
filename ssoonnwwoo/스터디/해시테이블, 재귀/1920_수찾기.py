'''
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 
이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -2^31 보다 크거나 같고 2^31보다 작다.
'''
import sys
input = sys.stdin.readline

N = int(input())
mynum = list(map(int, input().split()))
mynum.sort()

M = int(input())
finding = list(map(int, input().split()))


def binary_search(data, start, end, target):
    mid = (start + end)//2
    if start > end:
        return False
    if data[mid] == target:
        return True
    elif data[mid] > target:
        return binary_search(data, start, mid-1, target)
    else:
        return binary_search(data, mid+1, end, target)

for i in finding:
    if binary_search(mynum, 0, N-1, i):
        print(1)
    else:
        print(0)