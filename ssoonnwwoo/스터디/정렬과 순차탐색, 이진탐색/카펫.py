def solution(brown, yellow):#$$$$$$$$노랑이 같은개수여도 모양에 따라서 갈색의 개수가 달라짐$$$$$$
    answer = []
    ali = [i for i in range(1, yellow+1) if yellow%i==0]#노랑의 약수가 곧 노랑의 모양을 결정함 
    wh_set = [[i, yellow//i] for i in ali]#약수 세트화==노랑의 모양(가로, 세로)세트화
    final_wh = [i for i in wh_set if i[0]>=i[1]]#가로가 세로보다 커야하므로 앞에가 큰놈들로 구성[6,1] [3,2]
    
    for i in final_wh:#노랑의 모양, 노랑(가로, 세로)이 i 
        w, h = i[0], i[1] 
        if brown == (w+2)*2 + h*2:#갈색으로 감쌀수 있는지 10 + 4
            answer.append(w+2)
            answer.append(h+2)
    
    return answer

print(solution(24, 24))