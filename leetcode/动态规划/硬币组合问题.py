#coding:utf-8

"""
给出不同面额的硬币以及一个总金额.
写一个方法来计算给出的总金额可以换取的最少的硬币数量.
如果已有硬币的任意组合均无法与总金额面额相等, 那么返回 -1.
"""

"""
输入：
[1, 2, 5]
11
输出： 3
解释： 11 = 5 + 5 + 1
可以使用动态规划的方法
使用递归的方法会存在重复计算，
使用动态规划把从1-11的总金额需要的最小银币数都算一遍就可以一次得到11块钱最小需要多少枚银币。
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 初始化数组
        dp=[float("inf")]*(amount+1)
        # 设定初始值
        dp[0]=0
        # 从1 开始，amount结束,由于range的特点range(1,3)输出的是[1,2]，所以需要amount+1
        for i in range(1,amount+1):
            for coin in coins:
                if(i-coin>=0 and dp[i-coin]!=float("inf")):
                    dp[i]=min(dp[i],dp[i-coin]+1)
        print(dp)
        if dp[amount]!=float("inf"):
            return dp[amount]
        else:
            return -1

s=Solution()
print(s.coinChange([1, 2, 5], 11))
