class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        int i,j;
        HashMap<Integer,Integer> cache=new HashMap<Integer,Integer>();
        int[]  a = new int[2];
        for(i = 0; i<nums.length; i++)
        {
            if(cache.containsKey(nums[i]))
            {
                a[0] = cache.get(nums[i]);
                a[1] = i;
                break;
            }
            else
                cache.put(target-nums[i],i);
        }
        return a;
    }
}