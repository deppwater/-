# 打印字符串的全排列
# 如'abc'的输出结果为：
# 'abc'  'acb'  'bac'  'bca'  'cab'  'cba'

help_li = []
help_set = set()


def printAll(arr, i, j):
    i += 1

    # help_set.add(tuple(arr[:]))
    if i == len(arr):
        # print('test')
        # help_set.add(tuple(arr[:]))
        # help_li.append(arr[:])
        # print(id(arr))
        i = 0
        j += 1
        # return

    if j == len(arr):
        help_set.add(tuple(arr[:]))
        return
    arr[j], arr[i] = arr[i], arr[j]
    printAll(arr, i, j)
    arr[j], arr[i] = arr[i], arr[j]
    printAll(arr, i, j)


printAll([1, 2, 3, 4, 5], 0, 0)
print(help_set)
print(len(help_set))
# print(help_li)
# print(len(help_li))
# a = set()
# for k in help_li:
#     a.add(tuple(k))
# print(a)
# print(len(a))


# 就是当指针指向第一个元素a时，它可以是其本身a(即和自己进行交换)，还可以和b，c进行交换，故有3种可能，当第一个元素a确定以后，指针移向第二位置，第二个位置可以和其本身b及其后的元素c进行交换，又可以形成两种排列，当指针指向第三个元素c的时候，这个时候其后没有元素了，此时，则确定了一组排列，输出。但是每次输出后要把数组恢复为原来的样子。

# 简单来说，它的思想即为，确定第1位，对n-1位进行全排列，确定第二位，对n-2位进行全排列。。。显然，这是一种递归的思想。


COUNT = 0


def perm(n, begin, end):
    global COUNT
    if begin >= end:
        print(n)
        COUNT += 1
    else:
        i = begin
        for num in range(begin, end):
            # print(num)
            # print('test', begin, end)
            n[num], n[i] = n[i], n[num]
            perm(n, begin + 1, end)
            n[num], n[i] = n[i], n[num]


n = [1, 2, 3]
perm(n, 0, len(n))
print(COUNT)