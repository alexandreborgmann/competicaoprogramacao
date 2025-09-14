select  sp.name
from salesperson sp
where
(select count(*)
from orders o,
     company c
where 
 o.com_id=c.com_id and
      o.sales_id=sp.sales_id and
      c.name='RED')=0