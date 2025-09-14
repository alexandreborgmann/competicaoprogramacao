select t.*, 
case
when x<y+z and y<x+z and z<x+y then
   'Yes'
else
   'No'
end triangle
from triangle t