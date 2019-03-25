# 在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组的小和。求一个数组的小和。
# 例子：
# [1,3,4,2,5]
# 1左边比1小的数，没有；
# 3左边比3小的数，1；
# 4左边比4小的数，1、3；
# 2左边比2小的数，1；
# 5左边比5小的数，1、3、4、2；
# 所以小和为1+1+3+1+1+3+4+2=16

"""
最简单的方法(对数器的方法):
每个数遍历一下数组 比较一下小的加起来 最后把每次遍历完的结果加起来
时间复杂度：O(n^2)
lists = [1,3,4,2,5]
用merge的思想：
类似于归并排序
只不过每次归并操作、排序操作必须在辅助数组进行
需要注意的是因为数组是从小到大的 所以排序并不影响小和的计算
仍然是用指针a和指针b分别指向需要归并的两个数组
当a位置的数<b位置的数的时候 小和=a*b指针右边的数的数量 然后将a指向的数加入辅助数组 a指针向右移动
当a>b时 将b指向的数加入辅助数组 b指针向右移动
直到a越界或b越界 将b或a中剩余的数加入辅助数组
将辅助数组中的数从本次递归过程中l所在的位置开始赋值给原数组
返回小和并循环进行上述过程
"""


def small_sum_2(x):
    # 判断数组是否有效
    if len(x) < 2:
        return 0
    return merge_sort(x, 0, len(x) - 1)


def merge_sort(x, l, r):
    if l == r:
        return 0
    # m = (l + r) // 2
    # 位运算比算术运算快很多 所以建议用位运算
    m = l + ((r - l) >> 1)
    return merge_sort(x, l, m) + merge_sort(x, m + 1, r) + merge(x, l, m, r)


def merge(x, l, m, r):
    sum_num = 0
    i = 0
    p0 = l
    p1 = m + 1
    # 构建辅助数组
    help_list = [None] * (r - l + 1)
    while p0 <= m and p1 <= r:
        if x[p0] < x[p1]:
            sum_num += x[p0] * (r - p1 + 1)
            help_list[i] = x[p0]
            i += 1
            p0 += 1
        else:
            help_list[i] = x[p1]
            i += 1
            p1 += 1
    while p0 <= m:
        help_list[i] = x[p0]
        i += 1
        p0 += 1
    while p1 <= r:
        help_list[i] = x[p1]
        i += 1
        p1 += 1

    for i in range(len(help_list)):
        x[l + i] = help_list[i]

    return sum_num


if __name__ == '__main__':
    lists = [1, 3, 4, 2, 5]
    result = small_sum_2(lists)
    print(result)

