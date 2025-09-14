    using System;
    
    class URI {
    
        static void Main(string[] args) { 
    
    		float a,b,c,media=0;
    
            a=float.Parse(Console.ReadLine());
    		b=float.Parse(Console.ReadLine());
			c=float.Parse(Console.ReadLine());

    
    		media = (a*2f+b*3f+c*5f)/10.0f;
    
    
            System.Console.WriteLine(String.Format( "MEDIA = {0:0.0}", media ));
                
        }
    
    }
	
