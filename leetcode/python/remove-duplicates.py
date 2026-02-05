class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)
        nums[:] = sorted(list(set_nums))
        return len(nums)
    