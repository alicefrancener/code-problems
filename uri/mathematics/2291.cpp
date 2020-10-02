/*
  problem: Divine Numbers
  url: https://www.urionlinejudge.com.br/judge/en/problems/view/2291
*/

#include <iostream> 
#include <vector> 

using namespace std;

vector<long long> divisores(long long n) {
    vector<long long> somaDivisoresAcumulada(n);
    for(long long i = 1; i <= n; i++){
        for (long long j = i; j <=n; j +=i){
            somaDivisoresAcumulada[j] += i;
        }
    }
    for(long long i = 1; i <=n; i++){
        somaDivisoresAcumulada[i] += somaDivisoresAcumulada[i-1];
    }
    return somaDivisoresAcumulada;
}

int main() {
    vector<long long> somaDivisoresAcumulada = divisores(1000000);
    long long n;
    
    cin >> n;
    while(n) {
        cout << somaDivisoresAcumulada[n] << endl;
        cin >> n;
    }
    return 0;
}
