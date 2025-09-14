#include <stdio.h>

int main() {
int NumeroFuncionario,HorasTrabalhadas;
double ValorHora,Salario;




scanf("%d", &NumeroFuncionario);
scanf("%d", &HorasTrabalhadas);
scanf("%lf", &ValorHora);

Salario = HorasTrabalhadas*ValorHora;

printf("NUMBER = %d\n",NumeroFuncionario);
printf("SALARY = U$ %0.2lf\n",Salario);
    
	return 0;
}

