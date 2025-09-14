#include <stdio.h>

int main() {
char NomeFuncionario[200];
double SalarioFixo,Vendas;

scanf("%s", NomeFuncionario);
scanf("%lf", &SalarioFixo);
scanf("%lf", &Vendas);


printf("TOTAL = R$ %0.2lf\n",SalarioFixo+(Vendas*0.15));
    
	return 0;
}
