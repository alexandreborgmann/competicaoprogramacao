select max(x.SecondHighestSalary) "SecondHighestSalary"
from (
select e.salary SecondHighestSalary,dense_rank() over (order by e.salary desc) rnum
from employee e
) x
where x.rnum=2