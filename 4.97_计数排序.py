"""
计数排序是具象化桶排序的一种
思路：
初始化数组： A = [2,5,3,0,2,3,0,3]
数组的最小值为min 最大值为max 长度为len
构建一个帮助数组B 长度为max-min+1
构建一个帮助数组C 长度为原数组长度
先遍历一次数组A 数组B每个位置对应数组A里的每个不同的值从小到大排列的个数 遍历到的数-min即代表B数组此位置的计数+1
然后遍历一遍数组B 将B数组每个位置改为统计A数组中小于等于此位置对应A数组中数的数量总和 具体操作为B数组自身与前面一个位置的数相加
倒序扫描数组A的元素x 依次将元素放置于输出序列C[y]位置 y为小于或者等于这个元素的个数 同时临时数组B[x]=B[x]-1
详细过程见下方注释
重复这个过程直至扫描到数组A的首位元素
"""


def counting_sort(collection):
    if not collection:
        return collection
    len_arr = len(collection)
    min_num = min(collection)
    max_num = max(collection)

    help_arr = [0] * (max_num - min_num + 1)
    output_arr = len_arr * ['']

    for i in collection:
        help_arr[i - min_num] += 1
    print(help_arr)
    # print(len(help_arr))

    for i in range(1, len(help_arr)):
        help_arr[i] = help_arr[i] + help_arr[i - 1]
        # while help_arr[i - 1] == 0:
        #     help_arr[i] = help_arr[i] + help_arr[i - 1]
        #     i -= 1
    print(help_arr)

    for i in reversed(range(len_arr)):
        # print(i)
        # 假设现在需要排序的是第6个位置上的数1 因为1对应的是数组help_arr中的第(1-min_num)位置即比1小的数有help_arr(1-0)=6个
        # 那么这个1就应该放在output_arr数组的6位置上 对应的help_arr(1-0)=6需要减1 因为这个6代表的是大于等于1的数的数量
        # 有一个数被填入相应位置 当然需要这个统计数字减少1 而最后的6和7不需要减少的原因在于他们代表的是各自对应的数字
        # 其他数字如1的减少并不影响小于等于他们的数的总和且他们对应的是起始的插入数字的位置
        # 下面这里要减1是因为前面代表的是统计数字 而数组坐标是从0开始的
        output_arr[help_arr[collection[i] - min_num] - 1] = collection[i]
        help_arr[collection[i] - min_num] -= 1

    return output_arr


if __name__ == '__main__':
    result = counting_sort([1, 0, 3, 1, 0, 1, 1])
    print(result)
    # import extra
    # extra.Testing.mainTest(10000, counting_sort)
