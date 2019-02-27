class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        cur_r, cur_c = len(nums), len(nums[0])
        if cur_r * cur_c != r * c:
            return nums
        
        new_row = []
        result = []
        for row in nums:
            for n in row:
                new_row.append(n)                    
                if len(new_row) == c:
                    result.append(new_row)
                    new_row = []
                
        
        return result
       
"""
public class Solution {
    public int[][] matrixReshape(int[][] nums, int r, int c) {
        int[][] res = new int[r][c];
        if (nums.length == 0 || r * c != nums.length * nums[0].length)
            return nums;
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums[0].length; j++) {
                res[count / c][count % c] = nums[i][j];
                count++;
            }
        }
        return res;
    }
}
"""
