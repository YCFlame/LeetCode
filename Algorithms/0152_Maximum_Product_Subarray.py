class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        rs = nums[0]
        imax = rs 
        imin = rs
        for i in nums[1:]:
            if i < 0:
                imax, imin = imin, imax
            
            imax = max(i, imax * i)
            imin = min(i, imin * i)
            rs = max(rs, imax)
        
        return rs

            
