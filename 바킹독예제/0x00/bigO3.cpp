//N�� �������̸�  1�� ��ȯ�ϰ� �������� �ƴϸ� 0�� ��ȯ�ϴ� �Լ��� �ۼ� N�� 10�� ������ �ڿ����̴�.

#include<iostream>

int func3(int N);

int main(void){
	printf("%d", func3(11));
	return 0;
} 

int func3(int N){
	for(int i = 1;i <= N;i++){
		if(i * i == N) return 1;
	}
	return 0;
}

//�ð� ���⵵�� O((root)N) 
