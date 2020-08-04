#include<stdio.h>

int main(){
	int dist;
	double L;
	scanf("%d %lf",&dist,&L);
	printf("%.3lf km/l\n",dist/L);
	return 0;
}