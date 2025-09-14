select contest_id, round(count(*)/(select count(*) from users)*100,2) percentage
from register r
group by contest_id
order by 2 desc,1