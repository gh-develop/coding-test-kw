#include<bits/stdc++.h>
using namespace std;
int road[1000010];
int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n, k;
	cin >> n >> k;
	fill(road, road + 100010, -1);
	road[n] = 0;
	queue<int> Q;
	Q.push(n);
	while(k != Q.front()){
		auto cur = Q.front(); Q.pop();
		for(auto nxt : {cur * 2, cur - 1, cur + 1}){		//������ ���� ���� �°� Ʋ���� ���� bfs������ �ƴ϶� ���ͽ�Ʈ�� ���� 
			if(nxt < 0 || nxt > 100010) continue;
			if(road[nxt] != -1) continue;
			Q.push(nxt);
			if(nxt != cur * 2)
				road[nxt] = road[cur] + 1;
			else
				road[nxt] = road[cur];
			
		}
	}
	cout << road[k] << '\n';
	return 0;
}
