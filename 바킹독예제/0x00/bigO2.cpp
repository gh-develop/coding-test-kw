//�־��� ���� N�� int �迭 arr ���� ���� 100�� ���� �ٸ� ��ġ�� �� ���Ұ� �����ϸ� 1�� ��ȯ �׷��� ������ 0 �� ��ȯ�ϴ� �Լ��� �ۼ� arr �� �� ���� 0�̻� 100���ϰ� N�� 1000�����̴�.

#include<iostream>

int func2(int arr[], int N);

int main(void){
	int a[5] = {1,2,99,4,7};
	printf("%d", func2(a, 5));
	return 0;
}

int func2(int arr[], int N){
	for(int i = 0;i < N - 1;i++){
		for(int j = i + 1;j < N;j++){
			if((arr[i] + arr[j]) == 100) return 1;
		}
	}
	return 0;
}

//�ð� ���⵵�� O(N^2) 
