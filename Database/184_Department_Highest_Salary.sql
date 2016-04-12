/*
 * 184_Department_Highest_Salary.sql
 * Copyright (C) 2016 yangchao <yangchao@ChaodeMac-mini.local>
 *
 * Distributed under terms of the MIT license.
 */

select t2.Name as Department, t1.Name as Employee, t1.Salary 
from Employee as t1 join Department as t2 on t1.DepartmentId=t2.Id 
where t1.Salary in 
(select max(t3.Salary) from Employee as t3 where t3.DepartmentId=t1.DepartmentId)
