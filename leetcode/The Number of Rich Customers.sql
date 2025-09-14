select count(distinct customer_id) rich_count
from store s
where s.amount>500