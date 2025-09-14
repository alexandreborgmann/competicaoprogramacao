select e.name "employee"
from employee e
where e.salary>(select max(salary)
                from employee g
                where g.id=e.managerid
)