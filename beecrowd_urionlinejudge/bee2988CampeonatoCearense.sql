beecrowd SQL | 2988
Campeonato Cearense
Gustavo Moraes BR Brasil

Timelimit: 1
O Campeonato Cearense de Futebol atrai milhares de torcedores todos os anos, você trabalha em um jornal e está encarregado de calcular a tabela de pontuação dos times. Mostre uma tabela com as seguintes colunas: o nome do time, número de partidas, vitórias, derrotas, empates e pontuação. Sabendo que a pontuação é calculada com cada vitória valendo 3 pontos, empate vale 1 e derrota rende 0. No final mostre sua tabela com a pontuação ordenada do maior para o menor.

Esquema
teams
Coluna	Tipo
id (PK)	integer
name	varchar (50)
   
matches
Coluna	Tipo
id (PK)	integer
team_1 (FK)	integer
team_2 (FK)	integer
team_1_goals	integer
team_2_goals	integer
 
Tabelas
teams
id	name
1	CEARA
2	FORTALEZA
3	GUARANY DE SOBRAL
4	FLORESTA
   
matches
id	team_1	team_2	team_1_goals	team_2_goals
1	4	1	0	4
2	3	2	0	1
3	1	3	3	0
4	3	4	0	1
5	1	2	0	0
6	2	4	2	1
 
Exemplo de saída
name	matches	victories	defeats	draws	score
CEARA	3	2	0	1	7
FORTALEZA	3	2	0	1	7
FLORESTA	3	1	2	0	3
GUARANY DE SOBRAL	3	0	3	0	0
 
 
SELECT x.name,
       x.matches,
       x.victories,
       x.defeats,
       x.draws,
       (x.victories * 3) + x.draws as score
FROM (
    SELECT x.name, 
           SUM(matches) as matches,
           SUM(victories) as victories,
           SUM(defeats) as defeats,
           SUM(draws) as draws
    FROM (
        SELECT t.name, 
               COUNT(*) as matches, 
               SUM(CASE WHEN m.team_1_goals > m.team_2_goals THEN 1 ELSE 0 END) as victories,
               SUM(CASE WHEN m.team_1_goals < m.team_2_goals THEN 1 ELSE 0 END) as defeats,
               SUM(CASE WHEN m.team_1_goals = m.team_2_goals THEN 1 ELSE 0 END) as draws
        FROM teams t
        INNER JOIN matches m ON t.id = m.team_1
        GROUP BY t.name
        
        UNION ALL
        
        SELECT t.name, 
               COUNT(*) as matches, 
               SUM(CASE WHEN m.team_2_goals > m.team_1_goals THEN 1 ELSE 0 END) as victories,
               SUM(CASE WHEN m.team_2_goals < m.team_1_goals THEN 1 ELSE 0 END) as defeats,
               SUM(CASE WHEN m.team_2_goals = m.team_1_goals THEN 1 ELSE 0 END) as draws
        FROM teams t
        INNER JOIN matches m ON t.id = m.team_2
        GROUP BY t.name
    ) x
    GROUP BY x.name
) x
ORDER BY score DESC;