"""
查找芒果经销商（名字里有mango的人）
"""
# 关系图：
from collections import deque

graph={}
graph["me"]=['bob','alice','claire']
graph['bob']=['anuj','peggy']
graph['alice']=[]
graph['claire']=['thom_mango','jonny']

def bfs_search():
    # 创建双向队列
    queue=deque()
    while queue:
