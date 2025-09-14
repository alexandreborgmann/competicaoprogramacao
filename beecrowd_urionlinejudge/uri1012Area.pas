program main;

var pi,atriangulo,acirculo,atrapezio,aquadrado,aretangulo,a,b,c : real;

Begin

   read(a);
   read(b);
   read(c);
   
pi := real(3.14159);
atriangulo := (a*c)/2.0;
acirculo := pi*(c*c);  
atrapezio :=  ((a+b)*c)/2.0;
aquadrado := b*b;
aretangulo := a*b;
   
writeln('TRIANGULO: ',atriangulo:1:3);
writeln('CIRCULO: ',acirculo:1:3);
writeln('TRAPEZIO: ',atrapezio:1:3);
writeln('QUADRADO: ',aquadrado:1:3);
writeln('RETANGULO: ',aretangulo:1:3);

end.