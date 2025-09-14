select user_id,max(time_stamp) last_stamp 
from logins
where trunc(time_stamp)>=to_date('01012020','ddmmyyyy') and trunc(time_stamp)<to_date('01012021','ddmmyyyy')
group by user_id