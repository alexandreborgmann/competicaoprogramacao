select x.id, to_char(x.visit_date,'yyyy-mm-dd') visit_date, x.people
from (
select s.*, lead(id) OVER (order by visit_date) id_proximo1,
            lead(id,2) OVER (order by visit_date) id_proximo2,
            lag(id) OVER (order by visit_date) id_anterior1,
            lag(id,2) OVER (order by visit_date) id_anterior2
from stadium s
where people>=100
order by s.id
) x
where 
      (id+1=id_proximo1 and id+2=id_proximo2)
       or (id+1=id_proximo1 and id-1=id_anterior1)
       or (id-1=id_anterior1 and id-2=id_anterior2)