select w.id
from weather w
where (select max(w1.temperature)
         from weather w1
        where w1.recorddate=w.recorddate-1)<w.temperature