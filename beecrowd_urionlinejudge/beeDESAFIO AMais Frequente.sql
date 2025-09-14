select x.amount most_frequent_value
from 
(select  vt1.amount,count(*) qtd
from value_table vt1
group by amount
order by vt1.amount desc
limit 1
) x