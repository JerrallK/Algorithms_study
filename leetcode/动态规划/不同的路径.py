#coding:utf-8
"""
描述
中文
English
有一个机器人的位于一个 m × n 个网格左上角。

机器人每一时刻只能向下或者向右移动一步。机器人试图达到网格的右下角。

问有多少条不同的路径？

n和m均不超过100
且答案保证在32位整数可表示范围内。

样例
Example 1:

Input: n = 1, m = 3
Output: 1
Explanation: Only one path to target position.
Example 2:

Input:  n = 3, m = 3
Output: 6
Explanation:
	D : Down
	R : Right
	1) DDRR
	2) DRDR
	3) DRRD
	4) RRDD
	5) RDRD
	6) RDDR
"""

class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        if m==1 or n ==1:
            return 1
        dp=[[float("inf")]*n]*m
        dp[0][0]=0
        for i in range(m):
            for j in range(n):
                if i==0 and j !=0:
                    dp[0][j]=1
                if j==0 and i != 0:
                    dp[i][0]=1
                if i!=0 and j!=0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        print dp
        return dp[m-1][n-1]

s=Solution()
print s.uniquePaths(40,50)