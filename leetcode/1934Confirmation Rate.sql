select x.user_id, round(case
                        when x.qtd_action=0 then
                           0
                        else
                           (x.qtd_action/(select count(*)
                                  from confirmations c1
                                  where c1.user_id=x.user_id))
                        end,2) confirmation_rate
from (
select s.user_id, sum(case
                      when action='confirmed' then
                         1
                      else
                         0
                      end
                    ) qtd_action
from signups s,
     Confirmations c
where c.user_id(+)=s.user_id
group by s.user_id
) x 