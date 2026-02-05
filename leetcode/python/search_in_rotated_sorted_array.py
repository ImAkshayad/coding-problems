from typing import List
class Solution:
    def binary_search(self,nums: List[int], low: int, high: int, target: int) -> int:     
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid -1
            else:
                return mid
        return -1
    def search_min_element(self, nums: List[int]) -> int :
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return low

    def search(self, nums: List[int], target: int) -> int:
        if nums[0] <= nums[len(nums) - 1]:
            return self.binary_search(nums, 0, len(nums)-1, target)
        else:
            pivot_index = self.search_min_element(nums)
            if nums[0] <= target:
                return self.binary_search(nums, 0, pivot_index - 1, target)
            else:
                return self.binary_search(nums, pivot_index, len(nums)-1, target)

