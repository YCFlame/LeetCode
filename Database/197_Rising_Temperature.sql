/*
 * 197_Rising_Temperature.sql
 * Copyright (C) 2016 yangchao <yangchao@localhost>
 *
 * Distributed under terms of the MIT license.
 */

select Id from Weather as w1 where w1.Temperature > (select Temperature from Weather where Date=DATE_ADD(w1.Date, interval -1 day))

-- vim:et
