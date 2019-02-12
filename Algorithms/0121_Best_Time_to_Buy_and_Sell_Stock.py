class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        if not prices:
            return 0
        
        result = 0        
        buy = prices[0]
        for i in prices[1:]:
            if i - buy > result:
                result = i - buy
            
            if i < buy:
                buy = i
                
        return result
