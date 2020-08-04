#include <iostream>
 
using namespace std;

typedef long long ll;

bool isPrime(ll n ) {
  if ((n < 2) || ((n > 2) && (n % 2 == 0))) return false;
  for (int i = 3; (i * i) <= n; i += 2) {
    if (isPrime( i )){
      if (n % i == 0) return false;
    }
  }
  return true;
}
 
int main() {
    ll n_casos;
    ll primo;
    cin >> n_casos;
    for(int i= 0; i < n_casos; i++){
      cin >> primo;
      if (isPrime(primo)){
        cout << "Prime\n";
      } else {
        cout << "Not Prime\n";
      }
    }
    return 0;
}