def solution(answers):
    count_1, count_2, count_3 = 0, 0, 0
    student_1 = [1, 2, 3, 4, 5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if student_1[i % 5] == answers[i]:
            count_1 += 1
        if student_2[i % 8] == answers[i]:
            count_2 += 1
        if student_3[i % 10] == answers[i]:
            count_3 += 1
        
    array = [count_1, count_2, count_3]
    result = []
    
    if max(array) == count_1:
        result.append(1)
    if max(array) == count_2:
        result.append(2)
    if max(array) == count_3:
        result.append(3)
                    
    return result
