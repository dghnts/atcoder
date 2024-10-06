#include<bits/stdc++.h>
using namespace std;

bool isprime(long long N){
	for(long long i=2; i*i <= N;i++){
		if (N%i == 0)return false;
	}

	return true;
}

int main(){
	int N;
	cin >> N;
	if(isprime(N)){
		cout << to_string(N)+"は素数です" << endl;
	}
	else
	{
		cout << to_string(N)+"は素数ではありません"<< endl;
	}
	return 0;
}
