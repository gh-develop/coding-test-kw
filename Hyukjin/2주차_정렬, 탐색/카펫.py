def solution(brown, yellow):
    if yellow == 1:
        return [3, 3]
    else:
        # yellow_list에 a * b = yellow의 a, b를 저장
        yellow_list = []
        for i in range(1, yellow):
            if yellow % i == 0:
                if i > (yellow // i):
                    break
                yellow_list.append([yellow // i, i])
                yellow_list.reverse()
        
        for ele in yellow_list:
            if (ele[0] + 2) * (ele[1] + 2) == brown + yellow:
                return [ele[0] + 2, ele[1] + 2]
