//N������ �ڿ��� �߿��� 3�̳� 5�� ������ �������� ������ ���� ��ȯ�ϴ� �Լ��� �ۼ�. 

#include<iostream>

using namespace std;

int func1(int num);

int main(void){
	printf("%d", func1(16));
	return 0;
}

int func1(int num){
	int sum = 0;
	
	for(int i = 1;i <= num;i++)
		if(i % 3 == 0 || i % 5 == 0) sum += i;
	
	return sum;
}

//�ð� ���⵵�� O(N) 
