//�־��� ���� N�� int �迭 arr���� ���� 100�� ���� �ٸ� ��ġ�� �� ���Ұ� �����ϸ� 1�� �������� ������ 0�� ��ȯ�ϴ� �Լ�
//func2(int arr[], int N)�� �ۼ��϶�. ar�� �� ���� 0 �̻� 100 �����̰� N�� 1000�����̴�.
#include<bits/stdc++.h>
using namespace std;

int func(int arr[], int N){
	int num_cnt[101] = {0};
	for(int i = 0;i < N;i++){
		if(num_cnt[100 - arr[i]]) return 1;
		num_cnt[arr[i]]++;
	}
	
	return 0;
} 

int main(void){
	int arr[5] = {1, 23, 53, 77, 60};
	int N = 5;
	printf("%d", func(arr, N));
	return 0;
}
