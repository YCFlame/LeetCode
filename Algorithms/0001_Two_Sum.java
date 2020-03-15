import java.util.HashMap; 

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] rs = {0, 0};
        for (int i = 0; i < nums.length; i++){
            if (map.containsKey(target - nums[i])){
                rs[0] = map.get(target - nums[i]);
                rs[1] = i;
                break;
            } else {
                map.put(nums[i], i);
            }
        }
        return rs;
    }
}
