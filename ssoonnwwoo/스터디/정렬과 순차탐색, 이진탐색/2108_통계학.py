'''문제 :
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 
통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 
단, N은 홀수라고 가정하자.
1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
'''

'''입력 : 
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 
그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.
'''

'''출력 : 
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.
'''
import sys
input = sys.stdin.readline
N = int(input())
nums = sorted([int(input()) for i in range(N)])

from collections import Counter#Counter 클래스는 리스트안 요소의 개수를 세어서 반환[(요소, 개수),(요소, 개수),(요소, 개수)...]
freq=Counter(nums).most_common()#Counter클래스의 most_common메서드: 빈도가 가장 많은 것부터 정렬, 빈도가 같을경우 값이 작은 것부터 정렬
if len(freq) > 1:#빈도 값이 여러개일때
    if freq[0][1] == freq[1][1]:#최빈값이 여러개일때  
        mode = freq[1][0]#두번째 최빈값
    else:#최빈값이 한개일때
        mode = freq[0][0]
else : mode = freq[0][0]#빈도값이 한개일때


print("{0:.0f}".format(sum(nums)/len(nums)))#산술평균
print(nums[(len(nums)-1)//2])#중앙값
print(mode)#최빈값
print(nums[-1]-nums[0])#범위