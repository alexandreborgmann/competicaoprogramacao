select product_id, year first_year, quantity, price
from sales s
where s.year=(select min(s1.year) 
                from sales s1
            where s1.product_id=s.product_id)