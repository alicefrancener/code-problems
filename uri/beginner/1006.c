/*
  author: Alice Francener
  problem: Average 2
  url: https://www.urionlinejudge.com.br/judge/en/problems/view/1006
*/

#include <stdio.h>

int main()
{
	double a, b, c, media;
	scanf("%lf %lf %lf", &a, &b, &c);
	media = (2.0 * a + 3.0 * b + 5.0 * c) / 10.0;
	printf("MEDIA = %.1lf\n", media);
	return 0;
}