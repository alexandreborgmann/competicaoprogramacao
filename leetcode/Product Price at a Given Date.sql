select product_id,  nvl((select max(new_price)
                      from products p1
                      where p1.product_id=x.product_id and
                            p1.change_date=(select max(p2.change_date)
                                            from  products p2
                                          where  p2.product_id=x.product_id and
                                                 p2.change_date<=to_date('2019-08-16','yyyy-mm-dd')
                            )      
)
                     ,10)  price
from (
select distinct product_id 
from products 
) x