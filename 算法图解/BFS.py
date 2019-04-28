"""
查找芒果经销商（名字里有mango的人）
"""
# 关系图：
from collections import deque

graph = {}
graph["me"] = ['bob', 'alice', 'claire']

graph['bob'] = ['anuj', 'peggy']
graph['anuj']=[]
graph['peggy']=[]

graph['alice'] = []

graph['claire'] = ['thom_mango', 'jonny']
graph['thom_mango']=['cat']
graph['jonny']=[]

graph['cat']=[]

def bfs_search(g,center, target):
    """
    使用广度优先搜索，搜索map中的target
    时间复杂度：O(V+E)，V为顶点数（vertice）E为Edge边数
    :param g: 要搜索哪个图
    :param center: 图的中心是谁
    :param target: 要搜索这个图中的哪个信息
    :return: 返回图中是否有这信息
    """

    # 创建双向队列
    search_queue = deque()
    search_queue += g[center]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        print(person)
        if person not in searched:
            if person == target:
                print('find '+person)
                return True
            else:
                searched.append(person)
                search_queue+=g[person]
                print(search_queue)
    return False

bfs_search(graph,'me','cat')