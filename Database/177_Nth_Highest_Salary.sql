/*
 * 177_Nth_Highest_Salary.sql
 * Copyright (C) 2016 yangchao <yangchao@ChaodeMac-mini.local>
 *
 * Distributed under terms of the MIT license.
 */

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N=N-1;
    RETURN (select DISTINCT Salary from Employee order by Salary desc limit N,1);
END

-- vim:et
