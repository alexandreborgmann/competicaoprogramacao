select distinct to_char(c.visited_on,'yyyy-mm-dd') "visited_on", 
               (select sum(c1.amount)
                  from customer c1
                 where c1.visited_on between c.visited_on-6 and c.visited_on) "amount",
              round((select sum(c1.amount)
                       from customer c1
                      where c1.visited_on between c.visited_on-6 and c.visited_on)/7,2) "average_amount"
from customer c
where (select min(c2.visited_on)
         from customer c2
       )+6<=c.visited_on
order by 1
