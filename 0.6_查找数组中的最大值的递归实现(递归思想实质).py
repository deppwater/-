"""
递归函数：
递归函数的本质就是系统在帮你压栈
每一次调用自身函数都是在等子过程返回
压的栈里包含了当前的所有信息：
当前程序运行到了第几行 调用自身函数时传入的所有的参数和变量 系统指针等
然后运行子过程
如果子过程还要调用自身函数 重复上述操作
当触发判断结束条件return时 从压好的栈里开始弹出
根据当前弹出的信息继续从之前压入栈时候的状态运行整个函数
在例子中则是继续运行maxRight = getMax(arr, mid + 1, R)
之后重复压栈和弹出的操作 直到回到运行该函数的状态并得到返回值之后
此时假设只运行一次maxRight = getMax(arr, mid + 1, R)就达到递归返回条件
那么程序会继续往下执行return max(maxLeft, maxRight)
即return此时得到的maxRight和进入这个函数状态前得到的maxLeft中的最大值
过程中max(maxLeft, maxRight)是可能作为maxLeft = getMax(arr, L, mid)的返回值的
这个返回值会与当前的状态一起被压入maxRight = getMax(arr, mid + 1, R)

存疑：
递归主函数写法过程：
可以先按顺序写需要递归操作的数组
return想要得到的结果
"""
"""
master公式：
T(N)=aT(N/b)+O(n^d)
其中N为样本量
N/b为子问题(过程)的样本量
a子过程发生的次数
d除去调用子过程之外剩下的代价(时间复杂度)
分治过程中不考虑常数(即数组为奇数个时左右差一个数或有限个数的数) 只考虑规模(但分的时候还是几乎N/2)
下面的过程中 b=2, a=2, d=0
如果满足上面的式子 那么复杂度为:
1) log(b,a)[表示log以b为底a的对数] > d -> 复杂度为O(N^log(b,a))
2) log(b,a) = d -> 复杂度为O(N^d * logN)
3) log(b,a) < d -> 复杂度为O(N^d)
公式适用范围：
只要满足划分的子过程的规模是一样的就可以使用
后面的O(n^d)不一定要满足公式 也可以是O(N*logN)等 属于特例
绝大部分递归都可以使用这个公式
"""


def getMax(arr, L, R):
    if L == R:
        return arr[L]

    mid = int((L + R) / 2)
    maxLeft = getMax(arr, L, mid)
    maxRight = getMax(arr, mid + 1, R)
    return max(maxLeft, maxRight)


arr = [9, 1, 2, 3, 4, 5, 6, 7, 8]
result = getMax(arr, 0, len(arr) - 1)
print(result)
