#include<bits/stdc++.h>
using namespace std;
int n, m;
int arr[10];
bool vis[10];

void func(int k){
	if(k == m){
		for(int i = 0;i < m;i++)
			cout << arr[i] << ' ';
		cout << '\n';
	}
	for(int i = 1;i <= n;i++){
		if(!vis[i]){
			if(k != 0 && arr[k-1] > i) continue;
			arr[k] = i;
			vis[i] = 1;
			func(k+1);
			vis[i] = 0;
		}
	}
}

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> n >> m;
	func(0);
	return 0;
}
