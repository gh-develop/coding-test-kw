#include<bits/stdc++.h>
using namespace std;

bool vis1[40];	//���� 
bool vis2[40];	//������ ������ �Ʒ� �밢�� 
bool vis3[40];	//���� �Ʒ� ������ �� �밢�� 

int n;
int cnt;
void func(int cur){	//cur�� ������ ���� �����ϴ�. 
	if(cur == n){
		cnt++;
		return;
	}
	for(int i = 0;i < n;i++){
		if(vis1[i] || vis2[cur+i] || vis3[cur-i+n-1]) continue;
		vis1[i] = 1;
		vis2[cur+i] = 1;
		vis3[cur-i+n-1] = 1;
		func(cur+1);
		vis1[i] = 0;
		vis2[cur+i] = 0;
		vis3[cur-i+n-1] = 0;
	}
}
int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> n;
	func(0);
	cout << cnt;
	return 0; 
}
