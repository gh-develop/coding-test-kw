# 현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
# 인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
# location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.

#예제 6개의 문서(A, B, C, D, E, F)가 인쇄 대기목록에 있고 중요도가 1 1 9 1 1 1 이므로 C D E F A B 순으로 인쇄합니다.

# [2, 1, 3, 2]	2	1
# [1, 1, 9, 1, 1, 1]	0	5
# from collections import deque
# import sys
# sys.stdin = open('PG프린터_in.txt','r')

# priorities = [2, 1, 3, 2]
# location = 2
# list = [2,3,3,2]
#
# priorities = [1, 1, 9, 1, 1, 1]
# location = 1


# test = deque(list)
# test.append(test.popleft())
# print(test[0] >= max(test))
from collections import deque

def solution(priorities, location):
    answer = 0
    stop = 1
    deq = deque(priorities)
    while stop:
        if deq[0] >= max(deq):
            if location == 0:
                answer += 1
                stop = 0
            else:
                deq.popleft()
                answer += 1
                location -= 1
        else:
            deq.append(deq.popleft())
            if location == 0:
                location = len(deq)-1
            else:
                location -= 1
    return answer





