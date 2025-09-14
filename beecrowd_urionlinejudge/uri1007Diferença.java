import java.util.Scanner;

import java.io.IOException;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
 
     int A=0,B=0,C,D,X=0;
    

Scanner input = new Scanner(System.in);


A = input.nextInt();
B = input.nextInt();
C = input.nextInt();
D = input.nextInt();

X = (A*B-C*D);

 System.out.println("DIFERENCA = " + X);

 
    }
 
}
