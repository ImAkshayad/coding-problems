# Solution 1: Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

# Solution 2: Hash Table          
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_mapping = {}
        list_len = len(nums)
        # Map element with its index in hash table
        for i in range(list_len):
            index_mapping[nums[i]] = i
        
        for i in range(list_len):
            second_element = target - nums[i]
            if second_element in index_mapping and index_mapping[second_element] != i:
                return [i,index_mapping[second_element]]
        return []