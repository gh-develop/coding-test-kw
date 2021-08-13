#include<bits/stdc++.h>
using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n;
	cin >> n;
	vector<pair<int, int> > v;
	for(int i = 0;i < n;i++){
		int weight, height;
		cin >> weight >> height;
		v.push_back({weight, height});
	}
	for(int i = 0;i < n;i++){
		int cnt = 1;
		for(int j = 0;j < n;j++){
			if((v[i].first < v[j].first) && (v[i].second < v[j].second)) cnt++;
		}
		cout << cnt << ' ';
	}
	return 0;
}
