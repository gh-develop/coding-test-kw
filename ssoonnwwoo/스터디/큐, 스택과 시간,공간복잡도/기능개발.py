def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        cnt = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            cnt +=1
        days.append(cnt)#days에 각 기능 개발완료까지 남은 일수 추가
    
    head = 0
    while days:
        c=0
        head  = days.pop(0)#days의 맨 앞 요소를 pop해서 head에 할당
        c+=1
        if not days:
            answer.append(c)
            continue

        while head >= days[0]:#head가 days의 맨 앞 요소보다 크거나 같을때-->같이 배포가능한 기능 탐색5, 10, 1, 1, 20, 1
            days.pop(0)
            c+=1
            if not days:
                answer.append(c)
                break
        else:
            answer.append(c)
            
    return answer

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))