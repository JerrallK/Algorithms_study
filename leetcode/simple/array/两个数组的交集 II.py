class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums = []
        # return list(set(nums1) & set(nums2))
        if len(nums1) <= len(nums2):
            nums1,nums2=nums1,nums2
        else:
            nums1,nums2=nums2,nums1
        for i in nums1:
            if i in nums2:
                if i not in nums:
                    for j in range(min(nums2.count(i),nums1.count(i))):
                        nums.append(i)
        return nums



s=Solution()
print(s.intersect([1,2,2,1],[2,2]))