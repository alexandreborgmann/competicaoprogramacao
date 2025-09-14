    using System;
    
    class URI {
    
        static void Main(string[] args) { 


String  NomeFuncionario;
double SalarioFixo,Vendas;


        NomeFuncionario=Console.ReadLine();
        SalarioFixo=float.Parse(Console.ReadLine());
        Vendas=float.Parse(Console.ReadLine());
    

            System.Console.WriteLine(String.Format( "TOTAL = R$ {0:0.00}",SalarioFixo+(Vendas*0.15)));
                
        }
    
    }


