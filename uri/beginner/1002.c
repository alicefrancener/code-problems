/*
	author: Alice Francener
	problem: Area of a Circle
	url: https://www.urionlinejudge.com.br/judge/en/problems/view/1002
*/


#include<stdio.h>

int main(){
	double raio,pi=3.14159,area;
	scanf("%lf",&raio);
	area=(raio*raio)*pi;
	printf("A=%.4lf\n",area);
	return 0;
}