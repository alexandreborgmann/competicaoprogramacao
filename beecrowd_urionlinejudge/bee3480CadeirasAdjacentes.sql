beecrowd SQL
Cadeiras Adjacentes
Gustavo Moraes BR Brasil

Timelimit: 1
Encontre as cadeiras adjacentes e disponíveis de cada fila da sala de aula. A primeira coluna do resultado deve conter o identificador da fila, a segunda coluna o número da cadeira da esquerda e a terceira o número da cadeira da direita. O resultado deve estar ordenado pelo valor da segunda coluna do resultado (left).

 



Esquema
chairs
Coluna	Tipo
id	numeric
queue	numeric
available	boolean
 
Tabelas
chairs
id	queue	available
1	1	FALSE
2	1	FALSE
3	1	TRUE
4	1	FALSE
5	1	FALSE
6	1	FALSE
7	1	TRUE
8	1	TRUE
9	2	TRUE
10	2	FALSE
11	2	TRUE
12	2	TRUE
13	2	FALSE
14	2	TRUE
15	2	TRUE
16	2	FALSE
17	3	TRUE
18	3	FALSE
19	3	TRUE
20	3	FALSE
21	3	TRUE
22	3	TRUE
23	3	FALSE
24	3	FALSE
25	4	TRUE
26	4	FALSE
27	4	FALSE
28	4	TRUE
29	4	TRUE
30	4	FALSE
31	4	FALSE
32	4	TRUE
 
Exemplo de saída
queue	left	right
1	7	8
2	11	12
2	14	15
3	21	22
4	28	29
 
SBBD 2023 - 3a Maratona SQL

SELECT *
FROM (
    SELECT queue, id AS left, 
    (SELECT c1.id
     FROM chairs c1
     WHERE c1.queue = c.queue 
       AND c1.id = c.id + 1 
       AND c1.available = true
    ) AS right
    FROM chairs c
    WHERE c.available = true
) x
WHERE x.right IS NOT NULL 
ORDER BY left;