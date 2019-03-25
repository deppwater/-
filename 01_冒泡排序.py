import extra


def bubble_sort(alist):
    """
    冒泡排序：
    每次从队列开头取一个元素跟紧挨着的下一个元素比较
    如果前者大则进行交换 反之不交换
    这样每次最后的一个值都是当前比较过程得到的最大值 且每次比较使需要进行比较的数减少一个

    时间复杂度为 ------ O(n^2)
    最优时间复杂度 ---- O(n)
    平均时间复杂度 ---- O(n^2)
    所需辅助空间 ------ O(1)
    稳定性 ----------- 稳定(即相同数字的顺序没有改变)
    :return:
    """
    """
    鸡尾酒排序：
    与冒泡排序的不同处在于从低到高然后从高到低
    可以得到比冒泡排序稍微好一点的效能
    """
    n = len(alist)
    while n > 1:
        # 加入count判断是否进行了交换操作 若果没有则证明数组已有序
        count = 0
        for i in range(n - 1):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        print(alist)
        if count == 0:
            return alist
        n -= 1
    return alist


list1 = [8, 11, 3, 5, 2, 1, 9, 7, 4]
result = bubble_sort(list1)
print(result)

# 用对数器验证
# extra.Testing.mainTest(10000, bubble_sort)
