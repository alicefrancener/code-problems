/*
	author: Alice Francener
	problem: Bank Line
	url: https://www.urionlinejudge.com.br/judge/en/problems/view/1537
*/

#include <iostream>
using namespace std;

int main()
{
  unsigned long long n_pessoas;
  unsigned long long combinacoes;

  cin >> n_pessoas;
  while (n_pessoas)
  {

    combinacoes = 1;

    for (unsigned long long i = 4; i <= n_pessoas; i++)
    {
      combinacoes = (combinacoes * i) % 1000000009;
    }

    cout << combinacoes << '\n';
    cin >> n_pessoas;
  }

  return 0;
}