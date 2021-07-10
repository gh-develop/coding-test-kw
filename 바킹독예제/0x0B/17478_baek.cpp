#include<iostream>
using namespace std;
int cnt = 0;
void print(int n){
	for(int i = 0;i < n;i++) cout << "____";
}

void solve(int n){
	if(n == 0){
		print(cnt);
		cout << "\"����Լ��� ������?\"\n";						//�� �� ������ �򰥷��� ��� Ʋ�ȴ�.  
		print(cnt);
		cout << "\"����Լ��� �ڱ� �ڽ��� ȣ���ϴ� �Լ����\"\n";
		print(cnt);
		cout << "��� �亯�Ͽ���.\n";
		cnt--;
		return;
	}
	
	
	print(cnt);
	cout << "\"����Լ��� ������?\"\n";
	print(cnt);
	cout << "\"�� ����. �������� �� �� ����⿡ �̼��� ��� ������ ����� ������ �־���.\n";
	print(cnt);
	cout << "���� ������� ��� �� ���ο��� ������ ������ �߰�, ��� �����Ӱ� ����� �־���.\n";
	print(cnt);
	cout << "���� ���� ��κ� �ǾҴٰ� �ϳ�. �׷��� ��� ��, �� ���ο��� �� ���� ã�ƿͼ� ������.\"\n";
	cnt++;
	solve(n - 1);
	print(cnt);
	cout << "��� �亯�Ͽ���.\n";
	cnt--;
}

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n;
	cin >> n;
	cout << "��� �� ��ǻ�Ͱ��а� �л��� ������ �������� ã�ư� ������.\n";
	solve(n);
	return 0;
}
