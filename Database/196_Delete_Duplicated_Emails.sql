/*
 * 196_Delete_Duplicated_Emails.sql
 * Copyright (C) 2016 yangchao <yangchao@localhost>
 *
 * Distributed under terms of the MIT license.
 */

delete t1 from Person as t1, Person as t2 where t1.Email = t2.Email and t1.Id>t2.Id

-- vim:et
