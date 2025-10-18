Segundo Maior e Menor
Gustavo Moraes BR Brasil

Timelimit: 1
Encontre a cidade com a segunda maior população e em seguida a segunda menor população.

Esquema
cities
Coluna	Tipo
id	numeric
city_name	varchar(50)
population	numeric
 
Tabelas
cities
id	city_name	population
1	São Paulo	12396372
2	Rio de Janeiro	6775561
3	Brasília	3094325
4	Salvador	2900319
5	Fortaleza	2703391
6	Belo Horizonte	2530701
7	Manaus	2255903
8	Curitiba	1963726
9	Recife	1661017
10	Goiânia	1555626
11	Belém	1506420
12	Porto Alegre	1492530
 
Exemplo de saída
city_name	population
Rio de Janeiro	6775561
Belém	1506420
 
select c.city_name, c.population
from cities c
where c.id in
(
select x.id
from (
select id,dense_rank() over (order by population desc) rnum
from cities
) x
where x.rnum=2
union 
select x.id
from (
select id,dense_rank() over (order by population) rnum
from cities
) x
where x.rnum=2
)
order by c.population desc