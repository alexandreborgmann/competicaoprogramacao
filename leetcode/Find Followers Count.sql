select f.user_id, count(follower_id) followers_count
from followers f
group by f.user_id
order by user_id 