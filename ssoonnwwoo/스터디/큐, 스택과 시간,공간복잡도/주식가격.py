def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        cnt = 0
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                cnt+=1
            else:
                cnt+=1
                break
        answer.append(cnt)
        if i+1==len(prices)-1:#마지막 0처리
            answer.append(0)
    return answer

print(solution([1,2,3,2,3]))
