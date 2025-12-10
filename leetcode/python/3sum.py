class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        for i in range(len(sorted_nums)-2):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            target = -sorted_nums[i]
            j = i + 1
            k = len(sorted_nums)-1
            while j<k:
                current_sum = sorted_nums[j] + sorted_nums[k]
                if current_sum < target:
                    j += 1
                elif current_sum > target:
                    k -= 1
                else:
                    res.append([sorted_nums[i],sorted_nums[j],sorted_nums[k]])
                    j += 1
                    k -= 1
                    while j < k and sorted_nums[j] == sorted_nums[j-1]:
                        j += 1
        return res