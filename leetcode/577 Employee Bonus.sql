select *
from (
select  e.name,( select sum(b.bonus)
                  from bonus b
                 where b.empid=e.empid
                 ) bonus
from employee e
) x where x.bonus is null or x.bonus<1000