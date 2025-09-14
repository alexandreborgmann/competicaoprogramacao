    using System;
    
    class URI {
    
        static void Main(string[] args) { 

    
int CodigoPeca1,NumeroPecas1,CodigoPeca2,NumeroPecas2;
float ValorUnitarioPecas1,ValorUnitarioPecas2,ValorPagar;

			string[] texto = Console.ReadLine().Split(" ".ToCharArray());
            CodigoPeca1 = int.Parse(texto[0]);
			NumeroPecas1= int.Parse(texto[1]);
			ValorUnitarioPecas1 = float.Parse(texto[2]);

    		string[] texto1 = Console.ReadLine().Split(" ".ToCharArray());
            CodigoPeca2 = int.Parse(texto1[0]);
			NumeroPecas2= int.Parse(texto1[1]);
			ValorUnitarioPecas2 = float.Parse(texto1[2]);


ValorPagar = NumeroPecas1*ValorUnitarioPecas1 + NumeroPecas2*ValorUnitarioPecas2;    
    
            System.Console.WriteLine(String.Format( "VALOR A PAGAR: R$ {0:0.00}", ValorPagar));
                
        }
    
    }
        
