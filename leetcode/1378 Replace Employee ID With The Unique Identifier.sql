select u.unique_id, e.name
from employees e,
        employeeUNI u
where e.id=u.id(+)