def solution(priorities, location):
    answer = 0
    Tuples = [(data, data_index) for data_index, data in enumerate(priorities)]#enumerate이용해서 Tuplse에 우선순위와 고정인덱스 튜플 저장

    while Tuples:
        cur = Tuples.pop(0)#맨 앞 튜플을 pop해서 cur에 할당
        if any(cur[0] < Tuple[0] for Tuple in Tuples):#cur[0](우선순위)가 Tuples의 값들에서 하나라도 작은게 있으면 뒤로 추가
            Tuples.append(cur)
        else:
            answer+=1
            if cur[1]==location:
                return answer

print(solution([1,1,9,1,1,1], 4)) 