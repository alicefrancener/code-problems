#include<stdio.h>

int main(){
	int pc,npc,n=2;
	float vpc,total=0.0;
	while(n){
		scanf("%d %d %f",&pc,&npc,&vpc);
		total+=npc*vpc;
		n--;
	}
	printf("VALOR A PAGAR: R$ %.2f\n",total);
	return 0;
}