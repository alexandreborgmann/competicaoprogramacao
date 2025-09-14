select to_char(event_day,'yyyy-mm-dd') day,emp_id,sum(out_time-in_time) total_time
from employees
group by to_char(event_day,'yyyy-mm-dd') ,emp_id
order by to_char(event_day,'yyyy-mm-dd'),emp_id