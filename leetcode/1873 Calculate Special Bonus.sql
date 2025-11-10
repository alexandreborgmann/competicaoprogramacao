select e.employee_id, case
                      when mod(e.employee_id,2)<>0 and substr(e.name,1,1)<>'M' then
                         salary
                      else
                         0
                      end bonus
from employees e
order by e.employee_id