#리스트 내포 기능을 활용해 입력된 정수 값 5개의 평균을 출력하는 프로그램을 작성하십시오.
#      ㄴㄴㄴㄴ>[표현식 for 항목 in 반복가능객체 if 조건문]

data_list = [int(input()) for i in range(5)]
print("입력된 값 {0}의 평균은 {1}입니다.".format(data_list, sum(data_list)/len(data_list) ))