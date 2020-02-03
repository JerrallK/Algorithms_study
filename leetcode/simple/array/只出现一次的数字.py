"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

"""
可以通过异或运算
异或是一种基于二进制的位运算，用符号XOR或者 ^ 表示，
其运算法则是对运算符两侧数的每一个二进制位，
同值取0，异值取1。它与布尔运算的区别在于，当运算符两侧均为1时，布尔运算的结果为1，异或运算的结果为0。
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

s=Solution()
print s.singleNumber([1,1,2,3,3,2,4,4,5])