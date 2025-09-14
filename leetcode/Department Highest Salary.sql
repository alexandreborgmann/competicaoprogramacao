select d.name department, e.name employee, e.salary
from employee e,
     department d
where d.id=e.departmentid and
      e.salary=(select max(e1.salary)
                  from employee e1
                  where e1.departmentid=e.departmentid)
