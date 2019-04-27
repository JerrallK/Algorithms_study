import cProfile
import sys

sys.setrecursionlimit(100000000)

def sum(list):
    """
    递归计算list内的数字和
    :param list:
    :return:
    """
    if len(list) == 1:
        return list[0]
    else:
        return list[-1] + sum(list[:-1])


def count(list):
    if list == []:
        return 0
    else:
        return 1 + count(list[1:])

def max(list):
    if count(list)==1:
        return list[0]
    else:
        return list[0] if list[0]>list[1] else max(list[1:])


def qsort_mine(list):
    if len(list)==1:
        return list
    else:
        max_num=max(list)
        list.remove(max_num)
        return [max_num]+qsort_mine(list)
def qsort_rand(list):
    """
    O(n log n)的快排
    :param list:
    :return:
    """
    l=len(list)
    if l<2:
        return list
    else:
        rnd=random.randint(0,l-1)
        pivot=list[rnd]
        less=[i for i in list[:rnd]+list[rnd+1:] if i <=pivot]
        greater=[i for i in list[:rnd]+list[rnd+1:] if i > pivot]
        return qsort_rand(less)+ [pivot]+qsort_rand(greater)


def qsort2(list):
    """
    快速排序的效率和数列的原始顺序有关，
    假如选取的第一个选取的数字恰好是中位数，
    复杂度为调用栈高度*层数：O(n) * O(log n) = O(n log n)
    假如选取的第一个恰好是中位数，
    复杂度为：调用栈高度*层数：O(n) * O(n) = O(n^2)。

    综上为了减少原始数据带来的影响，只需每次随机选取基准值就可以达到O(n log n)
    参考qsort_rand的实现
    :param list:
    :return:
    """
    if len(list)<2:
        return list
    else:
        pivot=list[0]
        less=[i for i in list[1:] if i <=pivot]
        greater=[i for i in list[1:] if i > pivot]
        return qsort2(less) +[pivot]+qsort2(greater)


if __name__ == "__main__":

    import  random
    length=2000
    test_list = []
    for i in range(length):
        test_list.append(i)
    #test_list = [1, 2, 3,9, 4, 5]
    # print(sum(test_list))
    # print(count(test_list))
    # print(max(test_list))
    for i in [1,length/2]:
        test_list[0]=i
        print('-------------------------'+str(i)+'---------------------------')
        cProfile.run('qsort_rand(test_list)')
        cProfile.run('qsort2(test_list)')

