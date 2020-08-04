#include<stdio.h>

int main(){
	long unsigned int r;
	double pi=3.14159;
	scanf("%lu",&r);
	printf("VOLUME = %.3lf\n",(4.0/3.0)*pi*r*r*r);
	return 0;
}