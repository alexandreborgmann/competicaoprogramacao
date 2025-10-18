salario = float(input(""))
imposto=0
if salario>4500:
    imposto = (salario-4500)*.28 + 1500*.18 + 1000*0.08
if salario>=3000.01 and salario<=4500:
    imposto = (salario-3000)*.18 + 1000*.08
if salario>=2000.01 and salario<=3000:
   imposto = (salario-2000)*0.08
if imposto == 0:
    print('Isento')
else:
    print("R$ {:.2f}".format(imposto))