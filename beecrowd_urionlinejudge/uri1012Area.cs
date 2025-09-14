    using System;
    
    class URI {
    
        static void Main(string[] args) { 

double pi,atriangulo,acirculo,atrapezio,aquadrado,aretangulo,a,b,c;
    

			string[] texto = Console.ReadLine().Split(" ".ToCharArray());
            a = float.Parse(texto[0]);
			b = float.Parse(texto[1]);
			c = float.Parse(texto[2]);

pi = 3.14159;
atriangulo = (a*c)/2.0;
acirculo = pi*Math.Pow(c,2.0);
atrapezio =  ((a+b)*c)/2.0;
aquadrado = b*b;
aretangulo = a*b;



            System.Console.WriteLine(String.Format( "TRIANGULO: {0:0.000}",atriangulo));
            System.Console.WriteLine(String.Format( "CIRCULO: {0:0.000}",acirculo));
            System.Console.WriteLine(String.Format( "TRAPEZIO: {0:0.000}",atrapezio));
            System.Console.WriteLine(String.Format( "QUADRADO: {0:0.000}",aquadrado));
            System.Console.WriteLine(String.Format( "RETANGULO: {0:0.000}",aretangulo));

                
        }
    
    }



