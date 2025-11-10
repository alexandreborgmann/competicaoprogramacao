CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    select max(salary)
    into result
    from (
         select salary, dense_rank() over (order by salary desc) r
         from employee e
         ) x 
    where x.r=n;
    return result;
END;