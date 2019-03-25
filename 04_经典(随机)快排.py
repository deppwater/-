# 快速对一个数组进行排序
# 以最后一个数作为分解点 小的放左边 大的放右边
# lists = [2, 4, 10, 5, 11, 6, 8, 5, 0, 3, 5, 1, 9, 7]
# 快排是原地排序 最后直接返回原列表就可以了

"""
思路：
用荷兰国旗问题的思路 递归的方式解决
partition过程需要返回的是等于区域的范围
随机快排：
随机挑选一个数作为基准数
随机快排的时间复杂度是一个长期期望的复杂度 即O(N*logN)
注意：
1.想要绕过一个样本原本的数据状况(即假设原本样本很极端) 主要有两种方式
一是通过随机的方式 二是通过hash的方式
2.当两个排序算法指标(即时间复杂度)相同的时候 需要考察常数项
常数项跟算法的代码量有关 因此随机快排是最常用的算法
3.mergeSort由于使用while过多 相当于遍历了两次 而随机快排只有一个while
4.mergeSort的额外空间复杂度为O(N) 因为要生成一个等长的数组
随机快排的额外空间复杂度为O(logN）因为当每次递归划分区域的时候 由于基准数是随机选的
假设每次基准数都在中间位置 那么断点需要的额外空间就是logN 类似于二叉树
相较于经典快排 经典快排每次会选择最后一个数作为基准数 那么当数据情况最差的时候 需要的额外空间就为N
"""
import random

"""
荷兰国旗思路：
准备三个指针less和more less起始在-1位置 more起始在数组长度+1的位置 cur起始在0位置
遍历数组 判断cur位置的数与num的大小
当cur<num的时候 将cur所指的数与less的下一个位置交换 cur+=1 less+=1
当cur=num的时候 less不动 cur继续向右移动 即cur+=1
当cur>num的时候 将cur所指的数与more的前一个位置交换 但cur不动 less-=1 然后继续判断cur位置的新数
当cur与more指针相遇的时候 结束循环
"""


def static(lists):
    if len(lists) <= 1:
        return lists
    return quickSort(lists, 0, len(lists) - 1)


def quickSort(lists, L, R):
    if L < R:
        p = partition(lists, L, R)
        quickSort(lists, L, p[0] - 1)
        quickSort(lists, p[1] + 1, R)


def partition(lists, L, R):
    less = L - 1
    more = R + 1
    # 此处可以把more边界设为R 即让最后一个数位置一直不变 可以省去base_num这个变量
    # 这么做的思路是让R初始边界向左挪一格 那么在最后while执行完毕需要加一个more位置与R交换的操作
    cur = L
    # base_num = lists[R]
    base_num = lists[random.randint(L, R)]
    while cur < more:
        if lists[cur] < base_num:
            lists[less + 1], lists[cur] = lists[cur], lists[less + 1]
            less += 1
            cur += 1
        elif lists[cur] == base_num:
            cur += 1
        else:
            lists[more - 1], lists[cur] = lists[cur], lists[more - 1]
            more -= 1
    return [less + 1, more - 1]


if __name__ == '__main__':
    lists = [2, 4, 10, 5, 11, 6, 8, 5, 0, 3, 5, 1, 9, 7]
    static(lists)
    print(lists)
