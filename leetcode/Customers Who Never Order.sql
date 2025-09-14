select c.name "Customers"
from customers c
where (select count(*)
        from orders o
       where o.customerid=c.id)=0