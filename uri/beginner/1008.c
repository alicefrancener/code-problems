#include<stdio.h>

int main(){
	int n,horas;
	float valorhora,salario;
	scanf("%d %d %f",&n,&horas,&valorhora);
	salario=horas*valorhora;
	printf("NUMBER = %d\nSALARY = U$ %.2f\n",n,salario);
	return 0;
}