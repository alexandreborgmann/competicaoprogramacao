import java.util.Scanner;

import java.io.IOException;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
 
double PI = 3.14159,raio,area;
    

Scanner input = new Scanner(System.in);



raio = input.nextDouble();


area = PI*(raio*raio);

 System.out.printf("A=%.4f\n", area);


 
    }
 
}