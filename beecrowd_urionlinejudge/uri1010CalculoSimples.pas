program main;

var CodigoPeca1,NumeroPecas1,CodigoPeca2,NumeroPecas2 : integer;
var ValorUnitarioPecas1,ValorUnitarioPecas2,ValorPagar : real;

Begin

   read(CodigoPeca1);
   read(NumeroPecas1);
   read(ValorUnitarioPecas1);
   
   read(CodigoPeca2);
   read(NumeroPecas2);
   read(ValorUnitarioPecas2);
   
ValorPagar := NumeroPecas1*ValorUnitarioPecas1 + NumeroPecas2*ValorUnitarioPecas2;


   writeln('VALOR A PAGAR: R$ ',ValorPagar:1:2);
end.
