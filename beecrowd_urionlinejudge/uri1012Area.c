#include <stdio.h>
#include <math.h>

int main() {
double pi,atriangulo,acirculo,atrapezio,aquadrado,aretangulo,a,b,c;

scanf("%lf %lf %lf", &a,&b,&c);

pi = 3.14159f;
atriangulo = (a*c)/2.0f;
acirculo = pi*pow(c,2.0f);
atrapezio =  ((a+b)*c)/2.0f;
aquadrado = b*b;
aretangulo = a*b;

printf("TRIANGULO: %0.3lf\n",atriangulo);
printf("CIRCULO: %0.3lf\n",acirculo);
printf("TRAPEZIO: %0.3lf\n",atrapezio);
printf("QUADRADO: %0.3lf\n",aquadrado);
printf("RETANGULO: %0.3lf\n",aretangulo);

    
	return 0;
}
