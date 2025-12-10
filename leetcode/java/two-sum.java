// Solution 1: Brute Force
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        for(int i = 0; i < n-1; i++)
        {
            for(int j = i + 1; j < n; j++)
            {
                if(nums[i] + nums[j] == target)
                {
                    return new int[]{i,j};
                }
            }
        }
        return new int[]{};
    }
}

// Solution 2: Hash Table
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> index_mapping = new HashMap<>();
        int list_len = nums.length;

        // Map element with its index in hash table
        for(int i = 0; i < list_len; i++)
        {
            index_mapping.put(nums[i],i);
        }

        for(int i = 0; i < list_len-1; i++)
        {
            int second_element = target - nums[i];
            if(index_mapping.containsKey(second_element) && index_mapping.get(second_element) != i)
            {
                return new int[]{i, index_mapping.get(second_element)};
            }
        }
        return new int[]{};
    }
}
