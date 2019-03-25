# 给定一个数组arr，和一个数num，请把小于等于num的数放在数组的左边，大于num的数放在数组的右边。
# 要求额外空间复杂度O(1)，时间复杂度O(N)

"""
思路：
假设数组范围是L到R
设置一个指针X 起始位置为-1
遍历整个数组
当数组的数小于等于给定的num时 将这个数与X的下一个位置交换 然后X向右移动一格
如果大于则不进行交换操作 此时X位置不变 数组继续进行遍历操作
0-X所代表的区域就是小于等于区域
"""


def small_holland(lists, num):
    x = -1
    cur = len(lists)
    for i in range(cur):
        if lists[i] <= num:
            lists[x + 1], lists[i] = lists[i], lists[x + 1]
            x += 1
    return lists


result = small_holland([1, 3, 5, 7, 9, 8, 6, 4, 2], 5)
print(result)
