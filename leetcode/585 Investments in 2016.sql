select round(sum(tiv_2016),2)  "tiv_2016"
from Insurance i
where 
(select count(*)
   from Insurance i1
   where i1.tiv_2015=i.tiv_2015 )>=2 and
 (select count(*)
   from  Insurance i2
   where i2.pid<>i.pid and i2.lat=i.lat and i2.lon=i.lon
         )=0