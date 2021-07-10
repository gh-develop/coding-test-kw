#include<bits/stdc++.h>
using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	list<char> l;
	string str;
	cin >> str;
	for(auto c : str) l.push_back(c);
	int cnt;
	cin >> cnt;
	auto cursor = l.end();
	while(cnt--){
		char op;
		cin >> op;
		if(op == 'P'){
			char add;
			cin >> add;
			l.insert(cursor, add);
		}
		else if(op == 'L'){
			if(cursor != l.begin()) cursor--;
		}
		else if(op == 'D'){
			if(cursor != l.end()) cursor++;
		}
		else{
			if(cursor != l.begin()){
				cursor--;
				cursor = l.erase(cursor);
			}
		}
	}
	
	for(auto c : l) cout << c;
	return 0;
}

//L Ŀ���� �������� ��ĭ �ű�(�Ǿ��̸� ����)	D Ŀ���� ���������� ��ĭ �ű� (�ǵڸ� ����) B Ŀ�� ���ʿ� �ִ� ���ڸ� ������(�Ǿ��̸� ����) P $ $��� ���ڸ� Ŀ�� ���ʿ� �߰� 
