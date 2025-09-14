select username "Div 2 Ranklist"
from results r 
where r.rating>=1600 and r.rating<2000
order by score desc