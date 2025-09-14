#include <iostream>
#include<iomanip>
#include <stdio.h>

using namespace std;

int main() {

int NumeroFuncionario,HorasTrabalhadas;
double ValorHora,Salario;

cin >>NumeroFuncionario >>HorasTrabalhadas >>ValorHora;

Salario = HorasTrabalhadas*ValorHora;

printf("NUMBER = %d\n",NumeroFuncionario);
printf("SALARY = U$ %0.2lf\n",Salario);

    
	return 0;
}
