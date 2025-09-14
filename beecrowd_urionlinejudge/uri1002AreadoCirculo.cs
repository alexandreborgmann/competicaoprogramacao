using System;

class URI {

    static void Main(string[] args) { 

        double PI = 3.14159,raio,area;

        raio=double.Parse(Console.ReadLine());

        area = PI*(raio*raio);


        System.Console.WriteLine(String.Format( "A={0:#.0000}", area ));
            
    }

}
    
