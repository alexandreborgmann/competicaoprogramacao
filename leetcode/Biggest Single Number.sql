select max(num) num
from (
select num, count(*) qtd
from MyNumbers mn
group by num
) x 
where qtd=1