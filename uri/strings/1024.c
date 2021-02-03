/*
	author: Alice Francener
	problem: 1024 - Encryption
	description: https://www.urionlinejudge.com.br/judge/en/problems/view/1024
*/

#include <stdio.h>

int main()
{
  int n, i, j, k, m;
  char crip[10000], cripIn[10000];
  scanf("%d", &n);
  getchar();
  while (n--)
  {
    //ler string de caracter
    i = 0;
    while ((crip[i] = getchar()) != '\n')
    {
      //1. letras maisculas e minusculas (descolar 3 posicoes para direita)
      if ((crip[i] >= 'A' && crip[i] <= 'Z') || (crip[i] >= 'a' && crip[i] <= 'z'))
      {
        crip[i] = crip[i] + 3;
      }
      i++;
    }
    //2. inverter string
    k = 0;
    for (j = (i - 1); j >= 0; j--)
    {
      cripIn[k] = crip[j];
      k++;
    }
    //3. metade string (descolar uma posicao para esquerda)
    m = i / 2;
    for (j = m; j < i; j++)
    {
      cripIn[j] = cripIn[j] - 1;
    }
    //imprimir string
    for (j = 0; j < i; j++)
    {
      printf("%c", cripIn[j]);
    }
    printf("\n");
  }
  return 0;
}
