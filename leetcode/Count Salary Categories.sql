select 'Low Salary' category, count(*) accounts_count 
from accounts a
where a.income<20000
union all
select 'Average Salary' category, count(*) accounts_count 
from accounts a
where income>=20000 and income<=50000 
union all
select 'High Salary' category, count(*) accounts_count 
from accounts a
where income>50000