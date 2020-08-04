/*
	author: Alice Francener
	problem: Average 1
	url: https://www.urionlinejudge.com.br/judge/en/problems/view/1005
*/

#include<stdio.h>

int main(){
	double a,b,media;
	scanf("%lf %lf",&a,&b);
	media=(3.5*a+7.5*b)/11.0;
	printf("MEDIA = %.5lf\n",media);
	return 0;
}