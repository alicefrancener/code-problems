/*
  author: Alice Francener
  problem: Generating Fast, Sorted Permutation
  url: https://www.urionlinejudge.com.br/judge/en/problems/view/1401
  refs: http://www.cplusplus.com/reference/algorithm/next_permutation/?kw=next_permutation
*/

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
  int casos;
  string letras;
  cin >> casos;

  while (casos)
  {
    cin >> letras;
    sort(letras.begin(), letras.end());
    do
    {
      cout << letras << '\n';
    } while (next_permutation(letras.begin(), letras.end()));
    cout << '\n';

    casos--;
  }

  return 0;
}