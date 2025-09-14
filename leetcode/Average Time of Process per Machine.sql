select machine_id, round(sum(timestampdif)/count(*),3) processing_time 
from (
select a.machine_id, a.process_id, max(a.timestamp)-min(a.timestamp) timestampdif
from activity a
group by a.machine_id, a.process_id 
order by  a.machine_id, a.process_id 
) x
group by machine_id