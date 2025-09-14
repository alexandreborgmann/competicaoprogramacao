select u.user_id, upper(substr(name,1,1))||lower(substr(name,2)) name 
from users u
order by user_id