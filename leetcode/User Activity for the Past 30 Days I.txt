SELECT to_char(a.activity_date,'yyyy-mm-dd') "day",count(distinct user_id) "active_users"
FROM Activity a
WHERE TRUNC(a.activity_date)>TRUNC(to_date('2019-07-27','yyyy-mm-dd')-30) and 
      a.activity_date<=to_date('2019-07-27','yyyy-mm-dd')
group by to_char(a.activity_date,'yyyy-mm-dd')
ORDER BY 1