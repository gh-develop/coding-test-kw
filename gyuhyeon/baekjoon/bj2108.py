import sys
import math
sys.stdin = open('bj2108_in.txt', 'r')

n = int(input())

arr = []
ans = []
cnt = []
for _ in range(n):
    arr.append(int(input()))

# sorting
arr.sort()

for i in range(n):

    cnt.append([arr.count(arr[i]), arr[i]])

cnt.sort(key = lambda x: (-x[0], x[1]))
print(cnt)
# mean
ans.append(round(sum(arr)/n))
# middle
ans.append(arr[int((n-1)/2)])
#
print(arr.count(0))
print(ans)
# for i in range(n):


print(arr)
# indexes =[0]*100
# print(indexes)