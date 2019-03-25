"""
算法稳定性应用举例：
A B C 三个人 体重A>B>C 身高A>B=C
如果先按体重排序为A.B.C
再要按照身高排序且想保证B.C顺序不变而不是A.C.B
这时候就需要保证数据稳定
"""

"""
工程中的排序算法：
首先有两个大的分支
一是如果数据类型为单一的int、float、char等 那么首先选用快速排序 是因为基础类型 数据相同情况下顺序对结果不产生影响
二是如果数据类型为自定义类型 如一个学生类(包括身高体重等) 那么则首先选用归并排序 是因为自定义数据排序要考虑数据稳定性
其次如果数组长度很短 不管什么类型都会首先选择用插入排序 是因为插入排序的常数项极低 分界值大约为n=60
所以工程中可能会出现先用递归归并或者递归快速排序 加入判断当递归部分数据量小于60的时候采用插入排序 这样是效率最高的
"""

"""
有关排序问题的补充：
1，归并排序的额外空间复杂度可以变成O(1)，但是非常难，不
需要掌握，可以搜“归并排序 内部缓存法”
2，快速排序可以做到稳定性问题，但是非常难，不需要掌握，
可以搜“01 stable sort”
3，有一道题目，是奇数放在数组左边，偶数放在数组右边，还
要求原始的相对次序不变，碰到这个问题，可以怼面试官。面试
官非良人。
"""