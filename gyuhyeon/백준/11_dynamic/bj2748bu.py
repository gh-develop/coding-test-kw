import sys
sys.stdin = open('bj2748_in.txt', 'r')


def fibonacci_bu(n):
    memo = [0,1]

    for i in range(2, n+1):
        memo.append(memo[i-1] + memo[i-2])

    return memo [-1]


n = int(input())
print(fibonacci_bu(n))