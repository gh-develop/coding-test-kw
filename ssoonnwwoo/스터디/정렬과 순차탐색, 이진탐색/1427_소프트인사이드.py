#배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
'''입력:
첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.
'''
'''출력:
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
'''
def selection_sort_reverse(l):
    for i in range(len(l)-1):
        maxi = i
        for j in range(i+1,len(l)):
            if l[maxi] < l[j]:
                maxi = j
        l[i], l[maxi] = l[maxi], l[i]
    return l


N = list(map(int,input()))#[4,3,2,1]
selection_sort_reverse(N)#[4,3,2,1]
N = list(map(str, N))#['4', '3', '2', '1']
N = ''.join(N)#4321
print(N)

