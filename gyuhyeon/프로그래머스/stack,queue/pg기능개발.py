import sys
import math
from collections import deque
sys.stdin = open('pg기능개발_in.txt', 'r')

# math.ceil(-3.14)
# progresses = [93, 30, 55]
# speeds = [1, 30, 5]

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

def solution(progresses, speeds):
    answer = []
    days = []
    completion = 100

    for i in range(len(progresses)):
        remain = completion - progresses[i]
        day = math.ceil(remain/speeds[i])
        days.append(day)

    deq = deque(days)

    while len(deq):
        value = deq.popleft()
        count = 1
        if len(deq) == 0:
            answer.append(count)
            break
        else:
            while value >= deq[0]:
                deq.popleft()
                count += 1
                if len(deq) == 0:
                    break

        answer.append(count)

    return answer

print(solution(progresses, speeds))