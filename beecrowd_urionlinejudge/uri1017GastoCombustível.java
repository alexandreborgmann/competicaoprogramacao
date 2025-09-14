import java.util.Scanner;

import java.io.IOException;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
 
     int A=0,B=0;
    

Scanner input = new Scanner(System.in);


A = input.nextInt();
B = input.nextInt();


 System.out.printf("%.3f\n",(A*B)/12.0);

 
    }
 
}

