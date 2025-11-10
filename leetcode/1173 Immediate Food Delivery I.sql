select round(sum(decode(order_date,customer_pref_delivery_date,1,0))/count(1)*100,2) immediate_percentage
from delivery 