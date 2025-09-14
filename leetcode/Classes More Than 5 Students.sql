select class
from (
select c.class,count(*) conta
from courses c
group by c.class
) x
where x.conta>=5