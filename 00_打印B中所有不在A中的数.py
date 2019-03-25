# 一个有序数组A，另一个无序数组B，请打印B中的所有不在A中的数，
# A数组长度为N，B数组长度为M。

# 算法流程1：对于数组B中的每一个数，都在A中通过遍历的方式找一下；
# 算法流程2：对于数组B中的每一个数，都在A中通过二分的方式找一下；
# 算法流程3：先把数组B排序，然后用类似外排的方式打印所有在A中出现的数；

"""
算法流程3思路：
先对B数组进行排序
添加两个指针a和b
a对应A数组 b对应B数组
当b指针指的数小于等于a指针指的数则b指针向右移动
当小于的时候打印b指针指的数再移动 等于的时候则不打印直接移动
若不满足上述情况a指针向右移动
不能同时移动指针 需要加判定条件
"""

"""
时间复杂度：
算法流程1：O(M * N)
算法流程2：O(M * logN)
算法流程3(排序+判断)：O(M * logM) + O(N + M)
当A数组很小B数组很大 算法2好 反之算法3好
"""

aList = [1, 3, 5, 8, 9, 10, 11]
bList = [11, 9, 12, 2, 13, 6, 14, 10, 8, 15, 1, 3]
cList = [1, 3, 5, 8, 9, 10, 11, 1, 3]


def printDiffNum(aList, bList):
    a_Node, b_Node = 0, 0
    bList.sort()
    help_li = list()
    while a_Node < len(aList) and b_Node < len(bList):
        if bList[b_Node] <= aList[a_Node]:
            if bList[b_Node] < aList[a_Node]:
                help_li.append(bList[b_Node])
                # a_Node -= 1
            b_Node += 1
        elif bList[b_Node] > aList[a_Node]:
            a_Node += 1
    help_li.extend(bList[b_Node:])
    return help_li


result = printDiffNum(aList, cList)
print(result)

