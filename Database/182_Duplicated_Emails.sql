/*
 * 182_Duplicated_Emails.sql
 * Copyright (C) 2016 yangchao <yangchao@localhost>
 *
 * Distributed under terms of the MIT license.
 */

select Email from Person group by Email having count(*) > 1 


-- vim:et
