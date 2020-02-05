#coding:utf-8
"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

"""
https://blog.csdn.net/fobdddf/article/details/9834811
可以通过异或运算(异或运算满足交换律)
异或是一种基于二进制的位运算，用符号XOR或者 ^ 表示，
其运算法则是对运算符两侧数的每一个二进制位，
同值取0，异值取1。它与布尔运算的区别在于，当运算符两侧均为1时，布尔运算的结果为1，异或运算的结果为0。
例如：3^4
0011(3) ^ 0100(4) = 0111 (7)
对于[1,1,2,3,3,2,4,4,5]
由于异或运算满足交换律：
所以相当于：[1,1,2,2,3,3,4,4,5]
A^A=0
A^0=A

"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        for i in nums:
           a^=i
        return a

s=Solution()
print s.singleNumber([1,1,2,3,3,2,4,4,5])