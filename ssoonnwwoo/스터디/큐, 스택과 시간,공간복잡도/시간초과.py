C = int(input())
for _ in range(C):
    S, N, T, L = input().split()
    N, T, L = map(int, [N, T, L])
    if S == 'O(N)':
        cal = N*T
    elif S == 'O(N^2)':
        cal = (N*T)**2
    elif S == 'O(N^3)':
        cal = (N*T)**3
    elif S == 'O(2^N)':
        cal = 2**(N*T)
    else:#????????????
        cal = 1
        for i in range(N*T,0,-1):
            cal *= i
            if cal > L*(10**8):
                break
    if cal > L*(10**8):
                print("TLE!")
    else :
        print("May Pass.")
   