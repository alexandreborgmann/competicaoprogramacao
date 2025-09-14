import java.util.Scanner;

import java.io.IOException;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
 
float a,b,media=0;

    

Scanner input = new Scanner(System.in);



a = input.nextFloat();
b = input.nextFloat();

    
    		media = (a*3.5f+b*7.5f)/11.0f;


 System.out.printf("MEDIA = %.5f\n", media);
 
    }
 
}

