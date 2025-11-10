select name, travelled_distance
from (
select  u.id,ltrim(rtrim(u.name)) name, sum(nvl(distance,0)) travelled_distance
from users u,
     rides r
where r.user_id(+)=u.id
group by u.id,u.name
) x
order by 2 desc, 1