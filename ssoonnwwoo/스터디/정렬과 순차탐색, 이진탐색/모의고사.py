
def solution(answers):
    answer = []
    giveup_math =[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]#수포자
    result = []#성적 모음
    for i in range(len(giveup_math)):#수포자 3명분 반복문
        correct = 0#한사람이 끝날때마다 맞은 개수 초기화
        for j in range(len(answers)):#문제 개수만큼 반복
            if answers[j] == giveup_math[i][j%(len(giveup_math[i]))]:#예)수포자1이 풀때, 6번문제(5)의 답은 1(0), 7번문제(6)의 답은 2(1)
                correct+=1#문제를 싸이클 길이로 나눈 나머지가 같으면ㅇㅇ
        result.append(correct)#성적에 등록[0,2,2]
    most = max(result)#맞은개수에서 가장 큰수 most most =2
    
    for i in result:#1번, 2번, 3번성적 뽑음
        if i == most:#뽑은놈 성적이 1등이면
            answer.append(result.index(i)+1)#answer에 그놈 번호를 추가, 근데 공동 1등이 있으면 index가 첫번째 놈밖에 인식못함
            result[result.index(i)] = 0#공동1등이 있을경우를 대비해서 그놈 성적을 0으로 만듦
    
    return answer

print(solution([1,3,2,4,2]))