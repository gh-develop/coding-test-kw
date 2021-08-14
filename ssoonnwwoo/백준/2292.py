N = int(input())
a = 0
n = 0
while True:
    if N <= a:
        print(n)
        break
    a = 1 + 6*(sum(range(n+1)))    #1 + 6 * (0 + 1 + 2 + 3 + ... + n)
    n += 1
