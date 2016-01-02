/*
 * 175_Combine_Two_Tables.sql
 * Copyright (C) 2016 yangchao <yangchao@Chaos-MacBook-Pro.local>
 *
 * Distributed under terms of the MIT license.
 */

select t1.FirstName, t1.LastName, t2.City, t2.State from Person t1 left outer join Address t2 on t1.PersonId=t2.PersonId; 
