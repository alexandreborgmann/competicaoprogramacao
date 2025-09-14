import java.util.Scanner;

import java.io.IOException;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
 
float a,b,c,media=0;

    

Scanner input = new Scanner(System.in);



a = input.nextFloat();
b = input.nextFloat();
c = input.nextFloat();
    
    		media = (a*2f+b*3f+c*5f)/10.0f;


 System.out.printf("MEDIA = %.1f\n", media);
 
    }
 
}


