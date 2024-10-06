#include<bits/stdc++.h>

using namespace std;

int main(){
	long long N;
	cin >> N;
	for(int i=2;i*i<N;i++){
		if(N%i == 0){
			cout << i << " ";
			cout << N/i << " ";
		}
	}
	return 0;
}
