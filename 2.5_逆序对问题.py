# 逆序对问题
# 在一个数组中，左边的数如果比右边的数大，则折两个数构成一个逆序对，请打印所有逆序对

"""
逆序对问题：
思路类似于小和问题
只不过是倒序排序
倒叙需要修改的是添加help_list的时机
具体首先还是两个指针a和b
a负责左半部分 b负责右半部分
当a指针指向的数大于b指针指向的数 加入a a指针向右移动
否则加入b
特别需要注意的是添加逆序对的时机和范围
首先要默认数组是排好序的 即a负责的部分与b负责的部分分别已排好序
当a大于b的时候 a指向的数与此时b指向的数后面所有的数包括b本身分别组成逆序对 加入完之后a向右移动一格
当a小于b的时候 b向右移动一格
当a再次大于b的时候 逆序对一定是以a和此时b所在位置右边所有的数包括b本身组成
因为此时b部分b所在位置之前的数一定大于a此时所在位置的数
"""


def count_inversion(x):
    if len(x) < 2:
        return 0
    return merge_sort(x, 0, len(x) - 1)


def merge_sort(x, l, r):
    if l == r:
        return []
    m = l + ((r - l) >> 1)
    return merge_sort(x, l, m) + merge_sort(x, m + 1, r) + merge(x, l, m, r)


def merge(x, l, m, r):
    p0 = l
    p1 = m + 1
    out_put = list()
    help_list = [None] * (r - l + 1)
    i = 0
    while p0 <= m and p1 <= r:
        if x[p0] < x[p1]:
            help_list[i] = x[p1]
            i += 1
            p1 += 1
        else:
            for j in range(p1, r + 1):
                out_put.append([x[p0], x[j]])
            help_list[i] = x[p0]
            i += 1
            p0 += 1
    while p0 <= m:
        help_list[i] = x[p0]
        i += 1
        p0 += 1
        # for i in range(p0, r + 1):
        #     if lists[p0] > lists[i]:
        #         out_put.append([lists[p0], lists[i]])
    while p1 <= r:
        help_list[i] = x[p1]
        i += 1
        p1 += 1

    for i in range(len(help_list)):
        x[l + i] = help_list[i]

    return out_put


if __name__ == '__main__':
    lists = [6, 4, 3, 1, 2, 5]
    result = count_inversion(lists)
    print(result)
    print(lists)
