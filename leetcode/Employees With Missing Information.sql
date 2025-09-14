select e.employee_id
from employees e
where  (select count(*)
         from salaries s
        where s.employee_id=e.employee_id)=0
union
select s1.employee_id
from salaries s1
where (select count(*)
         from employees e1
         where e1.employee_id=s1.employee_id
         )=0
order by employee_id