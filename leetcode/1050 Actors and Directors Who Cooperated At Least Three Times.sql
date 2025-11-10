select  actor_id,director_id
from (
select actor_id,director_id,count(*)
from actordirector ad
group by actor_id,director_id
having count(*)>=3
) x