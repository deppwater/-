"""
假设有两个字符串m和n m和n分别代表一个字符串
目的是要把字符串拼起来 结果要得到字典序最小的那个组合

字典序：
将多个字符串的同一位置的字符按照26个字母的顺序进行比对 a最小 z最大
在比较两个长度不相等的字符串的时候 短的那个字符串要给后面补上比a还小的序就假设为0
那么'abc'和'b'比较的结果就是'abc'在前
但在组合的时候不能只考虑字符串的第一位的大小 如'ba'和'b' 只是比较序的话'b'在'ba'的前面
但实际上的结果'bba'要大于'bab'
因此要组合m和n得到字典序较小的组合就得比较m+n和n+m的大小

证明：
首先做出一个比较器 此题的比较策略就是贪心策略
先得证明这个比较策略有传递性 即假设：
a + b <= b + a
b + c <= c + b
那么一定得有 a + c <= c + a
证明过程：
如果将字母理解成k进制的数 那么a + b = a(代表的数) * k^(b的长度) + b(代表的数)
现在假设有 m(b) = k^(b的长度)
那么已知条件可改为：
a * m(b) + b <= b * m(a) + a   ①
b * m(c) + c <= c * m(b) + b   ②
①式两边同时-b然后再*c得到：
a * m(b) * c <= (b * m(a) + a - b) * c   ③
②式两边同时-b然后再*a得到：
(b * m(c) + c - b) * a <= c * m(b) * a   ④
③、④合并得到：
(b * m(c) + c - b) * a <= (b * m(a) + a - b) * c
即：
b * m(c) * a + ac - ab <= b * m(a) * c + ac - bc
两边同时-ac再/b化简得：
m(c) * a + c <=  m(a) * c + a
即： a + c <= c + a

继续证明：
还需要证明的是交换任意两个字符串都会得到更大的字典序
假设有一个字符串为：
...a,m1,m2...mk,b...
那么交换ab得到： ...b,m1,m2...mk,a...
证明过程：
由之前的结论
首先a与m1交换得到的...m1,a,m2...mk,b...一定大于交换之前的字典序
以此类推 经过2k次交换后得到的： ...b,m1,m2...mk,a...
字典序一定要比初始的字典序大

继续证明：
两两交换证明完毕之后还需证明三三交换、四四交换...

所以在做题的时候用对数器来证明结果对即可
"""