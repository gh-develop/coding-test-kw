'''
스택을 기반으로한 괄호검사 프로그램을 작성하세요
func = "{(A+B)-3}*5+[{cos(x+y)+7}-1]*4"
'''
func = "{(A+B)-3}*5+[{cos(x+y)+7}-1]*4"
a = [i for i in func if i in "[{()}]"]#괄호를 제외한 문자 날려버리기
stack = []
open_ = "[{("
close_= "]})"
for i in a:#a를 탐색?
    if i in open_:#i가 열리는 괄호면 Stack에 추가
        stack.append(i)
    else:#i가 닫히는 괄호면
        if open_.find(stack.pop()) != close_.find(i):#인덱싱을 이용한 방법과 딕셔너리 자료형을 이용할수도 있음 
            print("틀렸습니다.")
if not stack:
    print("수식의 괄호가 맞게 사용되었습니다!")
else:
    print("틀렸습니다.")
    