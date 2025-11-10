select p.project_id, round(sum(e.experience_years)/count(*),2) average_years
from employee e,
     project p
where p.employee_id=e.employee_id
group by p.project_id