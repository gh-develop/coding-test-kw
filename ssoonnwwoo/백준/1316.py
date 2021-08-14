n = int(input())
cnt = 0

for i in range(n):
    word = input()
    last = word[0]
    data = []
    if len(word) == 1 : continue       #한자리
    else:                              #여러자리
        for j in word[1:]:             #last에 word[0]으로 초기화 시켜놓고 word[1]부터 시작 
            if j not in data :         #data에 알파벳이 없고 
                if last == j:          #last랑 현재 알파벳이랑 같으면
                    continue           #그냥 지나가
                else :                 #last랑 현재 알파벳이랑 다르면       last가 바껴야 겠지?
                    data.append(last)  #일단 data에 last 추가하고
                    last = j           #last를 현재 알파벳으로
            else :                     #data에 알파벳이 있을때
                cnt += 1
                break
 
print(n - cnt)
