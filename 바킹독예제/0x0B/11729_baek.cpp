#include<bits/stdc++.h>
using namespace std;

void func(int a, int b, int n){
	if(n == 1){							//n���� ������ ����° ���� ��� �Űܾ��Ѵ�. n = 1�϶� �� �۵��Ѵ�. �׷��� �� ���̴�. 
		cout << a << ' ' << b << '\n';
		return ;
	}
	func(a, 6-a-b, n-1);				//n-1���� ������ 6-a-b�� ��� �ű�ٴ� ����� ��� 
	cout << a << ' ' << b << '\n';		//n��° ���� ū ������ b�� �ű�ٴ� ����� ��� 
	func(6-a-b, b, n-1);				//6-a-b�� �ִ� n-1���� ������ b�� �ű�ٴ� ����� ��� 
}

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int k;
	cin >> k;
	cout << (1<<k) - 1 << '\n';
	func(1, 3, k); 
	return 0;
}
