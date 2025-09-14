import java.util.Scanner;

import java.io.IOException;

public class Main {
 
    public static void main(String[] args) throws IOException {

int NumeroFuncionario,HorasTrabalhadas;
double ValorHora,Salario;
    
Scanner input = new Scanner(System.in);

NumeroFuncionario = input.nextInt();
HorasTrabalhadas = input.nextInt();
ValorHora = input.nextDouble();

Salario = HorasTrabalhadas*ValorHora;

System.out.printf("NUMBER = %d\n",NumeroFuncionario);
System.out.printf("SALARY = U$ %.2f\n",Salario);

    }
 
}
