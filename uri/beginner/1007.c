/*
  author: Alice Francener
  problem: Difference
  url: https://www.urionlinejudge.com.br/judge/en/problems/view/1007
*/

#include <stdio.h>

int main()
{
	int a, b, c, d, dif;
	scanf("%d %d %d %d", &a, &b, &c, &d);
	dif = (a * b - c * d);
	printf("DIFERENCA = %d\n", dif);
	return 0;
}