select x.score,dense_rank() over(ORDER BY score DESC) rank
from (
select s.score
from scores s
order by score desc
) x