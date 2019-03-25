def merge_sort(alist):
    """
    归并排序：
    单独申请一个等长的空间 用递归的方式拆分到不能再拆分然后排序
    具体排序时 申请两个指针A和B
    A和B分别处在两个要排序的列表开头位置
    如果最后拆分只剩一个元素 则自己跟自己排序
    每次将A和B中较小的加入help列表
    当A和B其中有一个的索引超过当前列表长度时 将另一个列表中剩余的元素加入help
    递归执行上述操作
    与快排不同之处在于快排是在原数组内部进行排序
    而归并排序是申请一个额外的空间来往里添加排好的元素
    所以在判断递归返回条件时 快排返回为空就行(代表返回上一步保存的操作)
    而归并排序需要返回最后一次排序(即最后一次拆分成一个元素)的结果

    master公式：T(N)=2T(N/2)+O(N)
    时间复杂度 ------- O(nlogn)
    最优时间复杂度 ---- O(nlogn)
    平均时间复杂度 ---- O(nlogn)
    所需辅助空间 ------ O(n)
    稳定性 ----------- 稳定(遇到相等的数总是拷贝左半区的)
    :return:
    归并排序快的实质在于没有废操作
    """
    left_node, right_node = 0, 0
    help_li = list()
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])

    while left_node < len(left_li) and right_node < len(right_li):
        if left_li[left_node] < right_li[right_node]:
            help_li.append(left_li[left_node])
            left_node += 1
        else:
            help_li.append(right_li[right_node])
            right_node += 1
    help_li += left_li[left_node:]
    help_li += right_li[right_node:]

    return help_li


list1 = [8, 11, 1, 3, 14, 15, 5, 2, 1, 9, 7, 12, 4, 13, 6, 10, 1]
result = merge_sort(list1)
print(result)
