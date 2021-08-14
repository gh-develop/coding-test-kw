n = int(input())
for i in range(n):
    data = input()
    cnt = 1
    score = 0
    for j in range(len(data)):
        if data[j] == 'O':
            if cnt > 1:
                score += cnt
                cnt+=1
            else : 
                score += 1
                cnt += 1
        else : 
            cnt = 1
    print(score)

