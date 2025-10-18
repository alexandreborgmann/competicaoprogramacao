beecrowd SQL | 2995
A Mensagem do Sensor
Gustavo Moraes BR Brasil

Timelimit: 1
â€‹
â€‹
Um sensor captura a temperatura do ambiente a cada minuto. Os registros tambÃ©m possuem um marcador, em que todas as vezes que a temperatura muda em relaÃ§Ã£o a Ãºltima captura esse marcador Ã© incrementado. Quando o sensor armazena 15 registros ele prepara uma mensagem para enviÃ¡-la o computador central. Para reduzir o tamanho da mensagem o sensor compacta os registros prÃ³ximos com a mesma temperatura e adiciona o nÃºmero de registros que foram compactados. Construa uma consulta para resolver esse problema, mostrando a temperatura e o nÃºmero de registros correspondente.

â€‹
â€‹
Esquema
records
Coluna	Tipo
id (PK)	integer
temperature	integer
mark	integer
 
Tabelas
records
id	temperature	mark
1	30	1
2	30	1
3	30	1
4	32	2
5	32	2
6	32	2
7	32	2
8	30	3
9	30	3
10	30	3
11	31	4
12	31	4
13	33	5
14	33	5
15	33	5
 
â€‹
â€‹
Exemplo de saÃ­da
â€‹  
temperature	number_of_records
30	3
32	4
30	3
31	2
33	3
 
â€‹
â€‹
â€‹ â€‹
 
SELECT 
    temperature,
    COUNT(*) as number_of_records
FROM (
    SELECT 
        id,
        temperature,
        mark,
        SUM(change_flag) OVER (ORDER BY id) as group_id
    FROM (
        SELECT 
            id,
            temperature,
            mark,
            CASE 
                WHEN temperature <> LAG(temperature, 1, temperature) OVER (ORDER BY id) THEN 1
                ELSE 0
            END as change_flag
        FROM records
    ) flagged
) grouped
GROUP BY temperature, group_id
ORDER BY MIN(id);
 