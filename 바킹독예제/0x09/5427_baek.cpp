//ó������ �ϳ��� ť�� ���� �ذ��Ϸ��ؼ� �Ӹ��� �ʹ� ���������� �ڵ嵵 ����������.
//����� ���� ť, �ҿ� ���� ť�� ���� ����� �ڵ带 �ۼ��ؾ� �߾���. 

#include<bits/stdc++.h>
using namespace std;
#define X first
#define Y second
string s[1002];
int bp[1002][1002];
int bf[1002][1002];
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};
int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	while(t--){
		int w, h;
		cin >> w >> h;
		for(int i = 0;i < h;i++){
			fill(bp[i], bp[i] + w, -1);
			fill(bf[i], bf[i] + w, -1);
		}
		for(int i = 0;i < h;i++)
			cin >> s[i];
		queue<pair<int, int> > Qp;
		queue<pair<int, int> > Qf;
		for(int i = 0;i < h;i++){
			for(int j = 0;j < w;j++){
				if(s[i][j] == '@'){
					bp[i][j] = 1;
					Qp.push({i, j});
				}
				else if(s[i][j] == '*'){
					bf[i][j] = 1;
					Qf.push({i, j});
				}
			}
		}
		
		//�� �� ������ �� �ð� ������� 
		while(!Qf.empty()){
			auto cur = Qf.front(); Qf.pop();
			for(int dir = 0;dir < 4;dir++){
				int nx = cur.X + dx[dir];
				int ny = cur.Y + dy[dir];
				if(nx < 0 || nx >= h || ny < 0 || ny >= w) continue;
				if(s[nx][ny] == '#' || bf[nx][ny] != -1) continue;
				Qf.push({nx, ny});
				bf[nx][ny] = bf[cur.X][cur.Y] + 1;
			}
		}
		bool is_right = false;
		while(!Qp.empty()){
			auto cur = Qp.front(); Qp.pop();
			for(int dir = 0;dir < 4;dir++){
				int nx = cur.X + dx[dir];
				int ny = cur.Y + dy[dir];
				if(nx < 0 || nx >= h || ny < 0 || ny >= w){
					is_right = true;
					cout << bp[cur.X][cur.Y] << '\n';
					break;
				}
				if(s[nx][ny] == '#' || bp[nx][ny] >= 0) continue;
				if(bf[nx][ny] != -1 && bf[nx][ny] <= bp[cur.X][cur.Y] + 1) continue;
				bp[nx][ny] = bp[cur.X][cur.Y] + 1;
				Qp.push({nx, ny});
			}
			if(is_right) break;
		}
		if(!is_right)
			cout << "IMPOSSIBLE" <<'\n';
	}
	return 0;
}
