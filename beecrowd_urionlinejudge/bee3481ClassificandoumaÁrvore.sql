beecrowd SQL
Classificando uma Árvore
Gustavo Moraes BR Brasil

Timelimit: 1
Dado a seguinte árvore binária balanceada armazenada na tabela nodes, classifique cada nó com os tipos LEAF, INNER, e ROOT. Apresente o resultado ordenado pelo valor do identificador do nó.

Esquema
nodes
Coluna	Tipo
node_id	numeric
pointer	numeric
 
Tabelas
nodes
node_id	pointer
50	30
50	75
30	15
30	35
15	1
15	20
35	32
35	40
1	null
20	null
32	null
40	null
75	60
75	90
60	55
60	70
90	80
90	95
55	null
70	null
80	null
95	null
 
Exemplo de saída
node_id	type
1	LEAF
15	INNER
20	LEAF
30	INNER
32	LEAF
35	INNER
40	LEAF
50	ROOT
55	LEAF
60	INNER
70	LEAF
75	INNER
80	LEAF
90	INNER
95	LEAF
 
SBBD 2023 - 3a Maratona SQL

WITH all_nodes AS (
    SELECT DISTINCT node_id AS id FROM nodes
    UNION 
    SELECT DISTINCT pointer AS id FROM nodes WHERE pointer IS NOT NULL
)
SELECT 
    n.id AS node_id,
    CASE 
        WHEN NOT EXISTS (SELECT 1 FROM nodes WHERE pointer = n.id) THEN 'ROOT'
        WHEN EXISTS (SELECT 1 FROM nodes WHERE node_id = n.id AND pointer IS NOT NULL) THEN 'INNER'
        ELSE 'LEAF'
    END AS type
FROM all_nodes n
ORDER BY n.id;
