select name
from employee e
where (select count(*)
         from employee e1
        where e1.managerId=e.id)>=5