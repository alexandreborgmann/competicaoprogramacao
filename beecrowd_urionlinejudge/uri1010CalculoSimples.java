import java.util.Scanner;

import java.io.IOException;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
 
int CodigoPeca1,NumeroPecas1,CodigoPeca2,NumeroPecas2;
float ValorUnitarioPecas1,ValorUnitarioPecas2,ValorPagar;
    
Scanner input = new Scanner(System.in);

CodigoPeca1 = input.nextInt();
NumeroPecas1 = input.nextInt();
ValorUnitarioPecas1 = input.nextFloat();

CodigoPeca2 = input.nextInt();
NumeroPecas2 = input.nextInt();
ValorUnitarioPecas2 = input.nextFloat();

ValorPagar = NumeroPecas1*ValorUnitarioPecas1 + NumeroPecas2*ValorUnitarioPecas2;
   

 System.out.printf("VALOR A PAGAR: R$ %.2f\n",ValorPagar);
 
    }
 
}

