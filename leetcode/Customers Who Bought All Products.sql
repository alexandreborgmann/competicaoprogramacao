select customer_id
from (
select c.customer_id, count(distinct product_key) conta_produto
from customer c
group by c.customer_id
) x 
where x.conta_produto=(select count(*) 
from product p)