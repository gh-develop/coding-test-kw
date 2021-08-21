def solution(priorities, location):
    print_list = [[priorities[i], i] for i in range(len(priorities))]
    cnt = 1  # 뽑는 횟수를 카운트

    while len(print_list) > 0:
        # print_list의 맨 왼쪽 원소를 꺼냄
        next_print = print_list.pop(0)

        try:
            priority = max(print_list)
        except:
            priority = [0, -1]

        # next_print의 priority보다 높은게 list에 있다면
        if next_print[0] < priority[0]:
            print_list.append(next_print)
        else:
            if next_print[1] == location:
                return cnt
            else:
                cnt += 1

        if len(print_list) == 1:
            return cnt
