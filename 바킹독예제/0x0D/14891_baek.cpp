#include<bits/stdc++.h>
using namespace std;
int k;
bool vis[4];	//����� �ѹ� ���� ������ ������ ���Ѵ�. ���� ����� ������ �� 0���� �ʱ�ȭ 
vector<deque<int> > v(4);

//���� �Ǵ� ������ ��Ϲ����� ������ �ִ��� Ȯ���ϴ� �Լ� 
void check_wheel(int cur, bool &left_side, bool &right_side){
	if(cur == 0 && !vis[cur+1]){	//1��° ����� �� 
		if(v[cur][2] != v[cur+1][6]) right_side = true;
	}
	else if(cur == 3 && !vis[cur-1]){ //4��° ��� �϶� 
		if(v[cur][6] != v[cur-1][2]) left_side = true;
	}
	else if(cur == 1 || cur == 2){	 //2, 3��° ��� �� �� 
		if(!vis[cur-1] && v[cur][6] != v[cur-1][2]) left_side = true;
		if(!vis[cur+1] && v[cur][2] != v[cur+1][6]) right_side = true;
	}
}

void func(int wheel, int dir){
	int cur = wheel-1;
	vis[cur] = true;
	bool left_side, right_side;	//�̳� ������ ��� Ʋ�ȴ�. �������� �������� ������ �������� 
	left_side = right_side = false;
	
	if(dir == 1){	//�ð���� ȸ�� 
		check_wheel(cur, left_side, right_side);
		int temp = v[cur].back();
		v[cur].pop_back();
		v[cur].push_front(temp);
	}
	else if(dir == -1){	//�ݽð� ���� ȸ�� 
		check_wheel(cur, left_side, right_side);
		int temp = v[cur].front();
		v[cur].pop_front();
		v[cur].push_back(temp);
	}
	
	if(left_side){
		if(dir == 1)
			func(wheel-1, -1);
		else if(dir == -1)
			func(wheel-1, 1);
	}
	if(right_side){
		if(dir == 1)
			func(wheel+1, -1);
		else if(dir == -1)
			func(wheel+1, 1);
	}
}

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	for(int i = 0;i < 32;i++){
		char c;
		cin >> c;
		if(i < 8) 		v[0].push_back(c-'0');
		else if(i < 16) v[1].push_back(c-'0');
		else if(i < 24) v[2].push_back(c-'0');
		else if(i < 32)	v[3].push_back(c-'0');
	}
	cin >> k;
	while(k--){
		int wheel, dir;
		cin >> wheel >> dir;
		func(wheel, dir);
		fill(vis, vis+4, 0);	//��� �湮 ���� �ʱ�ȭ 
	}
	int sum = 0;
	for(int i = 1;i < 5;i++){
		if(v[i-1][0])	//12�� ������ ��ϰ� 1�� �� ���� 
			sum += pow(2, i-1);
	}
	cout << sum;
	return 0;
}
