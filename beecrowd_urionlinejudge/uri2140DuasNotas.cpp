// uri2140DuasNotas.cpp : Este arquivo contém a função 'main'. A execução do programa começa e termina ali.
//

#include<iostream>

    using namespace std;

    int main()

    {
       int notas[6] = { 2, 5, 10, 20, 50, 100 };
       int compra, pagamento,troco,achou,i,j;

       while (1)
       {

           cin >> compra >> pagamento;

           if (compra == 0 and pagamento == 0)
               break;
           if (pagamento < compra or pagamento>10000)
           {
               cout << "valor invalido\n";
               continue;
           }
           troco = pagamento - compra;
           achou = 0;
           for(i=0;i<6;i++)
               for(j=0;j<6;j++)
                   if (troco == notas[i] + notas[j]) 
                       achou = 1;

           if (achou == 1)
               cout << "possible\n";
           else
               cout << "impossible\n";
       }

    }


