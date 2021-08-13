import sys
sys.stdin = open('ex_024_input.txt', 'r')


input_list = [int(input()) for _ in range(5)]
input_sum = 0

for i in input_list:
    input_sum += i

input_mean = input_sum/5



print("입력된 값 {0}의 평균은 {1}입니다.".format(input_list,input_mean))