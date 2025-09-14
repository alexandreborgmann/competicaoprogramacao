select x.email
from (
select p.email,count(*) 
from person p
where p.email is not null
group by p.email
having count(*)>=2
) x