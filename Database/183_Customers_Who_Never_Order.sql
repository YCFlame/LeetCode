/*
 * 183_Customers_Who_Never_Order.sql
 * Copyright (C) 2016 yangchao <yangchao@localhost>
 *
 * Distributed under terms of the MIT license.
 */

select Name as Customers from Customers as t1 where t1.Id not in (select CustomerId from Orders)


-- vim:et
