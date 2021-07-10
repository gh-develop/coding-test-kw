#include<bits/stdc++.h>
using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	cin.ignore();
	while(t--){
		string num;
		string temp = "";
		int sum = 0;
		
		getline(cin, num);
		
		for(int i = 0;i < num.length();i++){
			if(isdigit(num[i])){
				temp += num[i];
			}
			else{
				sum += stoi(temp);
				temp = "";
			}
		}
		sum += stoi(temp);
		cout << sum << '\n';
	}
	return 0;
}
