select *
from (
select id, sum(num) num
from (
select accepter_id id, count(*) num
from RequestAccepted ra
group by accepter_id 
union all
select requester_id id, count(*) num
from RequestAccepted 
group by requester_id 
) x
group by id
) w
where w.num=(
select z.num
  from (
select id, sum(num) num
from (
select accepter_id id, count(*) num
from RequestAccepted ra
group by accepter_id 
union all
select requester_id id, count(*) num
from RequestAccepted 
group by requester_id 
) y
group by id 
order by num desc,id
) z
where rownum=1
)