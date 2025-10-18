beecrowd SQL | 2994
Quanto Ganha um Médico?
Gustavo Moraes BR Brasil

Timelimit: 1
​
​
Você trabalha no setor de TI de um Hospital e precisa calcular a receita de pagamento de cada um dos médicos. Cada médico ganha 150$ por hora mais uma porcentagem dependendo do turno de trabalho, por exemplo, o médico Wellington trabalhou 1 hora no turno do dia, e 2 horas no turno da noite, logo seu salário semanal será: ( ( 1 * 150 ) + 1% ) + ( ( 2 * 150 ) + 15% ) = 496.5. Além disso, você pode usar a função round(value,1) para exibir os salários com 1 casa decimal e ordene o resultado do maior para o menor salário.

​
​
Esquema
doctors
Coluna	Tipo
id (PK)	integer
name	varchar (50)
 ​ 
work_shifts
Coluna	Tipo
id (PK)	integer
name	varchar(50)
bonus	numeric
   
attendances
Coluna	Tipo
id (PK)	integer
id_doctor (FK)	integer
hours	integer
id_work_shift (FK)	integer
  ​
​
Tabelas
doctors
id	name
1	Arlino
2	Tiago
3	Amanda
4	Wellington
 ​ ​ ​ 
work_shifts
id	name	bonus
1	nocturnal	15
2	afternoon	2
3	day	1
   
attendances
id	id_doctor	hours	id_work_shift
1	1	5	1
2	3	2	1
3	3	3	2
4	2	2	3
5	1	5	3
6	4	1	3
7	4	2	1
8	3	2	2
9	2	4	2
 
​
Exemplo de saída
​ 
name	salary
Arlino	1620.0
Amanda	1110.0
Tiago	915.0
Wellington	496.5
 
select d.name, round(sum((a.hours * 150 ) * (1+bonus/100)),1) as salary
from doctors d
inner join attendances a on d.id=a.id_doctor
inner join work_shifts ws on ws.id=a.id_work_shift
group by d.name
order by salary desc
 