import java.util.Scanner;

import java.io.IOException;

public class Main {
 
    public static void main(String[] args) throws IOException {

string NomeFuncionario;
double SalarioFixo,Vendas;
    
Scanner input = new Scanner(System.in);

NumeroFuncionario = input.nextLine();
SalarioFixo = input.nextDouble();
Vendas = input.nextDouble();

System.out.printf("TOTAL = R$ %.2f\n",SalarioFixo+(Vendas*0.15));

    }
 
}


