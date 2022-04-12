class ContainerWithMostWater {
    public int maxArea(int[] height) {
        int max=Integer.MIN_VALUE;

        int i=0,j=height.length-1;
        while(i<j)
        {
            max=Math.max(Math.min(height[i],height[j]) * (j-i) , max);

            if(height[i]<height[j]) i++;
            else if(height[j] < height[i]) j--;
            else if(height[i]==height[j])
            {
                i++;j--;
            }
            else
                break;
        }
        return max;
    }
}