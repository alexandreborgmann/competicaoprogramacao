    using System;
    
    class URI {
    
        static void Main(string[] args) { 

		int NumeroFuncionario,HorasTrabalhadas;
		double ValorHora,Salario;
    

        NumeroFuncionario=int.Parse(Console.ReadLine());
        HorasTrabalhadas=int.Parse(Console.ReadLine());
        ValorHora=float.Parse(Console.ReadLine());
    
		Salario = HorasTrabalhadas*ValorHora;

            System.Console.WriteLine(String.Format( "NUMBER = {0}",NumeroFuncionario));
            System.Console.WriteLine(String.Format( "SALARY = U$ {0:0.00}",Salario));
                
        }
    
    }


