#include<stdio.h>

int main(){
	char nome[30];
	double salario,vendas;
	scanf("%s%",&nome);
	scanf("%lf %lf",&salario,&vendas);
	salario+=vendas*0.15;
	printf("TOTAL = R$ %.2lf\n",salario);
	return 0;
}