from math import ceil


def solution(progresses, speeds):
    answer = []
    length = len(progresses)
    cnt = 1

    # 배포까지 걸리는 날짜, queue로 만들기
    days = [ceil((100 - progresses[i]) / speeds[i]) for i in range(length)]

    a = days.pop(0)

    while days:  # while len(days) == 0:
        b = days.pop(0)

        if a >= b:  # 앞의 작업의 남은 날이 같거나 더 오래 걸릴 때
            cnt += 1
        elif a < b: # 뒤의 작업이 더 오래 걸릴 때
            answer.append(cnt)
            cnt = 1
            a = b

        if len(days) == 0:
            answer.append(cnt)

    return answer
