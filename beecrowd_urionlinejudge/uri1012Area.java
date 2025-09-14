import java.util.Scanner;

import java.io.IOException;

import java.lang.Math; 
 
public class Main {
 
    public static void main(String[] args) throws IOException {

double pi,atriangulo,acirculo,atrapezio,aquadrado,aretangulo,a,b,c;
    
Scanner input = new Scanner(System.in);

a = input.nextDouble();
b = input.nextDouble();
c = input.nextDouble();

pi = 3.14159;
atriangulo = (a*c)/2.0;
acirculo = pi*Math.pow(c,2.0);
atrapezio =  ((a+b)*c)/2.0;
aquadrado = b*b;
aretangulo = a*b;


System.out.printf("TRIANGULO: %.3f\n",atriangulo);
System.out.printf("CIRCULO: %.3f\n",acirculo);
System.out.printf("TRAPEZIO: %.3f\n",atrapezio);
System.out.printf("QUADRADO: %.3f\n",aquadrado);
System.out.printf("RETANGULO: %.3f\n",aretangulo);
 
    }
 
}
