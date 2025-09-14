program main;
var NomeFuncionario : string;
var SalarioFixo,Vendas : real ;

Begin

   read(NomeFuncionario);
   read(SalarioFixo);
   read(Vendas);
   
   
writeln('TOTAL = R$ ',(SalarioFixo+(Vendas*real(0.15))):1:2);

end.
