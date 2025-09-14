select x.queue,x.left,x.right 
from (
select c.*, LAG(id) over (ORDER BY id,queue) left, lead(id) over (ORDER BY id,queue) right
from chairs c
order by id, queue
) x 
where x.available=TRUE
