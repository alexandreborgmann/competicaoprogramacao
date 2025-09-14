select y.person_name
from (
select  x.*
from (
select q.*, sum(weight) OVER (ORDER BY turn) AS soma, rownum rnum
from queue q
) x 
where x.soma<=1000 
order by soma desc
) y 
where rownum=1