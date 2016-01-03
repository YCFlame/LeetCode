/*
 * 176_Second_Highest_Salary.sql
 * Copyright (C) 2016 yangchao <yangchao@Chaos-MacBook-Pro.local>
 *
 * Distributed under terms of the MIT license.
 */

SELECT MAX(salary) FROM Employee WHERE Salary NOT IN ( SELECT Max(Salary) FROM Employee);
