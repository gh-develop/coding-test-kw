import sys
sys.stdin = open('bj2748_in.txt', 'r')


def fibonacci_td(n):
    if n < 2:
        return n

    if _memo[n] is None:
        _memo[n] = fibonacci_td(n-1) + fibonacci_td(n-2)

    return _memo[n]


_memo = [None] * 91
n = int(input())
print(fibonacci_td(n))