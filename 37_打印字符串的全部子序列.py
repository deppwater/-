# 打印一个字符串的全部子序列 包括空字符
# 例如'abc'的打印结果为：
# /  'a  '  /  ' b '  /  '  c'   /  'ab '  /  'a c'  /  ' bc'  /  'abc'  /
# 将尝试的想法变成代码就是写递归的能力
# 可以尝试画树的图来写递归


def printAll(string, i, res):
    if i == len(string):
        print(res)
        return
    printAll(string, i + 1, res)
    printAll(string, i + 1, res + string[i])


# printAll('abc', 0, '')
