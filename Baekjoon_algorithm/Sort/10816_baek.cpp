#include<bits/stdc++.h>
using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n, m;
	cin >> n;
	vector<int> arr(n);
	for(int i = 0;i < n;i++)
		cin >> arr[i];
	cin >> m;
	sort(arr.begin(), arr.end());
	for(int i = 0;i < m;i++){
		int num;
		cin >> num;
		//upper_bound�� �ش� ���� �ּ� +1 ���� �˾Ƽ� �����ߴ�. 
		cout << upper_bound(arr.begin(), arr.end(), num) - lower_bound(arr.begin(), arr.end(), num) << ' ';
	}
	return 0;
}
