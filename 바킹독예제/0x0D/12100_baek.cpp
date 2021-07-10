#include<bits/stdc++.h>
using namespace std;
int n;
int box[25][25];
int box2[25][25];

void turn(){
	int temp[25][25];
	for(int i = 0;i < n;i++)
		for(int j = 0;j < n;j++)
			temp[i][j] = box2[i][j];
	for(int i = 0;i < n;i++)
		for(int j = 0;j < n;j++)
			box2[i][j] = temp[n-1-j][i];
}

//���� ���� �̵���Ű�� �Լ� 
void func(int dir){
	while(dir--) turn();
	for(int i = 0;i < n;i++){
		int idx = 0;
		int temp[25] = {};
		for(int j = 0;j < n;j++){
			if(box2[i][j] == 0) continue;
			if(temp[idx] == 0) temp[idx] = box2[i][j];
			else if(temp[idx] == box2[i][j]) temp[idx++] *= 2;
			else temp[++idx] = box2[i][j];
		}
		for(int j = 0;j < n;j++) box2[i][j] = temp[j];
	}
}

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> n;
	int total = 0;
	//���� �Է¹ޱ� 
	for(int i = 0;i < n;i++)
		for(int j = 0;j < n;j++)
			cin >> box[i][j];
	//�ִ� 5�� �̵����Ѽ� �������ִ� ��� �ܿ��� ���� 4^5�̴�.4(�����¿� �����̴� �ܿ��Ǽ�) 
	for(int k = 0;k < 1024;k++){
		for(int i = 0;i < n;i++)
			for(int j = 0;j < n;j++)
				box2[i][j] = box[i][j];
		int brute = k;
		//�ִ� 5�� �̵��ϴ� ����� ���� 
		for(int i = 0;i < 5;i++){
			//4������ �̿��� �����¿� ���� �̵��� ������ ����
			//4�� ���� ���� ���� �̵��� ���������� �̵��� �������� ��Ÿ�� 
			int dir = brute%4;
			brute/=4;
			func(dir);
		}
		for(int i = 0;i < n;i++)
			for(int j = 0;j < n;j++)
				total = max(total, box2[i][j]);
	}
	cout << total;
	return 0;
}
