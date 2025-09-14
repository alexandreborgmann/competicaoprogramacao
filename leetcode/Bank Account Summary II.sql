
select u.name, sum(amount) balance
from users u,
     transactions t
where t.account=u.account
group by u.name
having sum(amount)>10000