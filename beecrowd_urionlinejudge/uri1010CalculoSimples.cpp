#include <iostream>
#include<iomanip>
#include <stdio.h>
using namespace std;

int main() {

int CodigoPeca1,NumeroPecas1,CodigoPeca2,NumeroPecas2;
float ValorUnitarioPecas1,ValorUnitarioPecas2,ValorPagar;

cin >>CodigoPeca1 >>NumeroPecas1 >>ValorUnitarioPecas1;
cin >>CodigoPeca2 >>NumeroPecas2 >>ValorUnitarioPecas2;

ValorPagar = NumeroPecas1*ValorUnitarioPecas1 + NumeroPecas2*ValorUnitarioPecas2;

printf("VALOR A PAGAR: R$ %.2f\n",ValorPagar);


    
	return 0;
}