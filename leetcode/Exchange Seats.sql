select 
     case
     when s.id=((select max(s1.id) from seat s1)) and mod(s.id,2)<>0 then
        s.id
     when mod(s.id,2)=0 then
        s.id-1
     else
        s.id+1
     end id, s.student
from seat s
order by 1