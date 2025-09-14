    using System;
    
    class URI {
    
        static void Main(string[] args) { 
    
    		float a,b,media=0;
    
            a=float.Parse(Console.ReadLine());
    		b=float.Parse(Console.ReadLine());
    
    		media = (a*3.5f+b*7.5f)/11.0f;
    
    
            System.Console.WriteLine(String.Format( "MEDIA = {0:0.00000}", media ));
                
        }
    
    }
        