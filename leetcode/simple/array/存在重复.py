class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if (len(nums) <= 1):
            return False
        for i in range(len(nums)):
            for j in nums[i+1:]:
                if nums[i] == j:
                    return True
        return False
s=Solution()
print s.containsDuplicate([3,1,2])