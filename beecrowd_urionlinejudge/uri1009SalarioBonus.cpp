#include <iostream>
#include<iomanip>
#include <stdio.h>

using namespace std;

int main() {

char NomeFuncionario[200];
double SalarioFixo,Vendas;

cin >>NomeFuncionario >>SalarioFixo >>Vendas;


printf("TOTAL = R$ %0.2lf\n",SalarioFixo+(Vendas*0.15));

    
	return 0;
}
