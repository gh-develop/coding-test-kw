#include<bits/stdc++.h>											//�ڵ��ƺ��� ���� ���� 
using namespace std;
int box[102][102][102];
int dh[6] = {0, 0, 0, 0, 1, -1};								//ó���� dh�� 3 dx dy�� ũ��� 4�� �ؼ� ���� ũ�Ⱑ �޶��µ� �����غ��� 6�����ϸ� ȥ���� ������. 
int dx[6] = {-1, 0, 1, 0, 0, 0};
int dy[6] = {0, 1, 0, -1, 0, 0};
int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int m, n, h;
	cin >> m >> n >> h;
	queue<tuple<int, int, int> > Q;								//������ bfs�ʹ� �޸� ���ڸ� 3���� ��� ���. �׷��� tuple�� ��� 
	bool isRight = false;
	for(int i = 0;i < h;i++){									//�� ó���� ���� �־���� ���ڸ� ���� �Է¹޾Ƽ� ������ ������� ���� �����ϴ��� ������ �ߴ�. ��� ���Ʒ� ������ ��� ������. 
		for(int j = 0;j < n;j++){
			for(int k = 0;k < m;k++){
				cin >> box[i][j][k];
				if(box[i][j][k] == 0) isRight = true;			//�� ���� �ʾ����� true 
				if(box[i][j][k] == 1)
					Q.push(make_tuple(i, j, k));				//�� ������ ���� �丶����� ��ġ ť�� ��´�. 
			}
		}
	}
	if(!isRight){												//ó������ �� ���� ���� 0�� ��� 
		cout << 0 << '\n';
		return 0;
	}
	
	while(!Q.empty()){
		int ch, cx, cy;
		tie(ch, cx, cy) = Q.front(); Q.pop();
		for(int dir = 0;dir < 6;dir++){
				int nh = ch + dh[dir];
				int nx = cx + dx[dir];
				int ny = cy + dy[dir];
				if(nx < 0 || nx >= n || ny < 0 || ny >= m || nh < 0 || nh >= h) continue;
				if(box[nh][nx][ny] != 0) continue;
				box[nh][nx][ny] = box[ch][cx][cy] + 1;			//�ٸ� ������ �丶����� ������ 1�� ���۵Ǿ���Ѵٰ� �����ؼ� ������ �ߴ�. 
				Q.push(make_tuple(nh, nx, ny));
			}
	}
	int day = 0;
	for(int i = 0;i < h;i++){
		for(int j = 0;j < n;j++){
			for(int k = 0;k < m;k++){
				day = max(day, box[i][j][k]);					//��Ÿ�� ������ �ڲٳ��� ���� ���̿� ���ؼ� ���ܻ��� ������ ó�� ���س��� �׷��� ���̿���. 
				if(!box[i][j][k]){
					cout << -1 << '\n';
					return 0;
				}
			}
		}
	}
	cout << day - 1 << '\n';									//1�� ���������� 1�� ������Ѵ�. 
	return 0;
}
