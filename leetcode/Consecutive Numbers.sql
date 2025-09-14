select distinct x.num ConsecutiveNums
from (
select num, lag(l.num) over(order by id) numProximo, lead(l.num) over(order by id) numAnterior
from logs l
) x
where  x.num=numProximo and x.num=numAnterior