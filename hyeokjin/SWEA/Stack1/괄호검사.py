# -*- coding: utf-8 -*-
"""
주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 
입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
 
정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

[입력]
3
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())

[출력]
#1 1
#2 1
#3 0

"""

T = int(input())

for test_case in range(1, T + 1):
    stack = []
    list1 = list(input())
    
    for i in list1:
        if i == '{' or i =='(':
            stack.append(i)
    
        if len(stack) > 0:
            if stack[-1] == '{'and i == '}':
                stack.pop(-1)
            elif stack[-1] != '{' and i == '}':
                print("#{0} {1}".format(test_case, 0))
                break
            if stack[-1] == '(' and i == ')':
                stack.pop(-1)
            elif stack[-1] != '(' and i == ')':
                print("#{0} {1}".format(test_case, 0))
                break
            
        elif len(stack) == 0 and i == '}' or i == ')':
            print("#{0} {1}".format(test_case, 0))
    
    if len(stack) == 0:
        print("#{0} {1}".format(test_case, 1))
    