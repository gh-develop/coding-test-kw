#include<bits/stdc++.h>
using namespace std;

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	stack<int> S;
	int height;
	int n;
	cin >> n;
	long long cnt = 0;
	while(n--){
		cin >> height;
		
		while(!S.empty()){
			if(S.top() <= height)			//������ �ߺ��� ���δٸ��̶�� ���̸� �����ٰ� �����߱� ������ Ʋ�ȴ�. 
				S.pop();
			else{
				cnt++;
				S.push(height);
				//���� ū �������� ������ŭ ���� �� 
				if(S.size() > 2)
					cnt += S.size() - 2;
				break;
			}
		}
		
		if(S.empty())
			S.push(height);
	}
	cout << cnt << '\n';
	return 0;
}
