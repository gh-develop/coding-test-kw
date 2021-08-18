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
def bubble_sort(l):
    for i in range(len(l)):
        swap =0
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                swap +=1
        if swap == 0:
            break 
    return l
N = int(input())
nums = [int(input()) for i in range(N)]
freq = [nums.count(i) for i in nums]
newnums = []
maxfreq = max(freq)
if freq.count(maxfreq) > 1:
    for a in range(len(freq)):
        if freq[a]==maxfreq:
            newnums.append(freq[a])
            freq[a] = 0
    mode = newnums[1]
else: mode = nums[freq.index(maxfreq)]
print("{0:.0f}".format(sum(nums)//len(nums)))
print(bubble_sort(nums)[(len(nums)-1)//2])
print(mode)
print(nums[-1]-nums[0])