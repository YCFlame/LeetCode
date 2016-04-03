/*
 * 181_Employees_Earning_More_Than_Their_Managers.sql
 * Copyright (C) 2016 yangchao <yangchao@localhost>
 *
 * Distributed under terms of the MIT license.
 */

SELECT Name from Employee as t1 where Salary > (SELECT Salary FROM Employee where Id=t1.ManagerId)

-- vim:et
