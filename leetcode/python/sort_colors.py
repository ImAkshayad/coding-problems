class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeroes_index = 0
        twos_index = len(nums) - 1
        ptr_ = 0

        while ptr_ <= twos_index:
            if nums[ptr_] < 1:
                nums[zeroes_index], nums[ptr_] = nums[ptr_], nums[zeroes_index]
                zeroes_index += 1
                ptr_ += 1
            elif nums[ptr_] > 1:
                nums[twos_index], nums[ptr_] = nums[ptr_], nums[twos_index]
                twos_index -= 1
                print(nums)
            else:
                ptr_ += 1