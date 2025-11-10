select s.student_id, s.student_name,su.subject_name,
   (select count(*)
      from examinations e
     where e.student_id=s.student_id and 
           e.subject_name=su.subject_name
   ) attended_exams
from students s,
     Subjects su
order by s.student_id,su.subject_name