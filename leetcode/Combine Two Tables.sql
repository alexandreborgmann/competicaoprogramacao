select firstName, lastName, city,  state
from  Person p,
      Address a
where p.personid=a.personid(+)