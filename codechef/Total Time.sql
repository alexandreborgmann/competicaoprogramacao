select sum(s.seconds) "Total Time"
from Submissions s
where s.seconds = (select min(s1.seconds)
                 from Submissions s1
                 where s1.problem_name=s.problem_name and
                       s1.verdict='Accepted')