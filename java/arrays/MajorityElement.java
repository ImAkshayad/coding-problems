public class MajorityElement {
    public int majorityElement(int[] nums) {
        int count=1, majority=nums[0];

        for(int i=1;i<nums.length;i++)
        {
            if(nums[i]==majority)
                count++;
            else
                count--;

            if(count==0)
            {
                count=1;
                majority=nums[i];
            }
        }
        return majority;
    }
}