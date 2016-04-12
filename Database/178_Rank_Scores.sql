/*
 * 178_Rank_Scores.sql
 * Copyright (C) 2016 yangchao <yangchao@ChaodeMac-mini.local>
 *
 * Distributed under terms of the MIT license.
 */

SELECT Score, rank FROM
(SELECT Score,
@curRank := IF(@prevRank = Score, @curRank, @incRank) AS rank, 
@incRank := IF(@prevRank = Score, @incRank, @incRank+1), 
@prevRank := Score
FROM Scores, (
SELECT @curRank :=0, @prevRank := NULL, @incRank := 1
) r 
ORDER BY Score desc) s
