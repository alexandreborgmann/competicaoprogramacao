select 
round(sum(
case
when customer_pref_delivery_date=order_date then
   1
else
   0
end)/count(*)*100,2) immediate_percentage
from delivery d
where d.order_date=(select min(d1.order_date)
                      from delivery d1 
                    where d1.customer_id=d.customer_id)
order by order_date