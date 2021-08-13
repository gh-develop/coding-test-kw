//���� �������µ� ���ڿ� �Է��� ��� �ؾ��ϳ����� ���� ��̴�. ������ ����� ���� �ʴ� ������ ���ľ߰ڴ�. 

#include<bits/stdc++.h>
using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	while(1){
		stack<char> S;					//������ �ݺ������� ����Ѵٸ� �ݺ��� �ȿ��ٰ� ������ ���� 
		bool isValid = true;
		string s;
		getline(cin, s);
		if(s == ".") break;				//string�̹Ƿ� ""���� �����־���Ѵ�. 
		for(auto c : s){
			if(c == '(' || c == '[') S.push(c);
			else if(c == ')'){
				if(S.empty() || S.top() != '('){
					isValid = false;
					break;
				}
				S.pop();
			}
			else if(c == ']'){
				if(S.empty() || S.top() != '['){
					isValid = false;
					break;
				}
				S.pop();
			}
		}
		if(!S.empty()) isValid = false;
			if(isValid)
				cout << "yes" << '\n';
			else
				cout << "no" << '\n';
	}
	return 0;
}
