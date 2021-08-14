N = int(input())

def hansu(n) :
    data = list(range(1,n+1))
    cnt = 0
    for i in data:
        num = list(map(int ,str(i)))
        if len(num) < 3:
            cnt += 1
        else : 
            if num[0]-num[1] == num[1]-num[2]:
             cnt += 1
    return cnt
print(hansu(N))