class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        rs = []
        end = 0
        while end < len(nums):
            start = end
            while end + 1 < len(nums) and nums[end] + 1 == nums[end + 1]:
                end += 1
            
            rs.append(str(nums[start]) if start == end else "%s->%s" % (nums[start], nums[end]))
            
            end += 1
            
        return rs
