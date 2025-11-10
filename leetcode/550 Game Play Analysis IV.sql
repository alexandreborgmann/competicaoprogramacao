with 
x as
(select count(distinct a.player_id) logs
from activity a
where a.event_date=(select min(a1.event_date)
                     from activity a1
                    where a1.player_id=a.player_id) 
      and (select count(*)
             from activity a2
            where a2.player_id=a.player_id and
                  a2.event_date=a.event_date+1
          )>0),
y as (
select count(distinct player_id) total
from activity)
select round(x.logs/y.total,2) fraction
from x,y