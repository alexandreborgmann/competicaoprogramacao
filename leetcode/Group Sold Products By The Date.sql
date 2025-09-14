SELECT to_char(sell_date,'yyyy-mm-dd')  "sell_date", 
       COUNT(PRODUCT) "num_sold",
       listagg(product, ',') within group ( order by 1 ) "products"
from (
       SELECT SELL_DATE, PRODUCT 
       FROM ( SELECT A.*, ROW_NUMBER() OVER(PARTITION BY SELL_DATE,product ORDER BY 1)TOP 
                FROM ACTIVITIES A
            ) WHERE TOP = 1
)
GROUP BY sell_date
order by sell_date