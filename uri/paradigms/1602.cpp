/*
	author: Alice Francener
	problem: 1602 - Hyperprimes
	description: https://www.urionlinejudge.com.br/judge/en/problems/view/1602
*/

#include <iostream>
#include <vector>

using namespace std;

vector<long long> divisores(long long n) {
    vector<long long> qtdDivisores(n);
    for(long long i = 1; i <= n; i++){
        for (long long j = i; j <=n; j +=i){
            qtdDivisores[j] += 1;
        }
    }
    return qtdDivisores;
}

vector<long long> hiperprimosAcumulados(long long n) {
    vector<long long> qtdDivisores = divisores(n);
    vector<long long> hiperprimos(n);
    
    for(long long i=2; i<=n;i++) {
        hiperprimos[i] += hiperprimos[i-1];
        if (qtdDivisores[qtdDivisores[i]] == 2) {
            hiperprimos[i] +=  1;
        }
    }
    return hiperprimos;
}

int main() {
    vector<long long> hiperprimos = hiperprimosAcumulados(2000000);
    long long n;
    while(cin >> n) {
        cout << hiperprimos[n] << endl;
    }
    return 0;
}
