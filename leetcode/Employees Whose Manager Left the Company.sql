select e.employee_id
from Employees e
where e.salary<30000 and
      ((select count(*)
         from Employees m
        where m.employee_id=e.manager_id)=0 and
        e.manager_id is not null
       )
order by 1