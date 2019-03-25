"""
输入：参数1，正数数组costs，参数2，正数数组profits，参数3，正数k，参数4，正数m
costs[i]表示i号项目的花费 profits[i]表示i号项目在扣除花费之后还能挣到的钱(利润)
k表示你不能并行只能串行的最多做k个项目 m表示你初始的资金
说明：你每做完一个项目，马上获得的收益，可以支持你去做下一个项目
输出：你最后获得的最大钱数

思路：
首先建立单独的项目 每个项目其中存入cost值与profit值
建立一个小跟堆存储cost 建立一个大根堆存储小跟堆中项目的profit
根据初始资金m确定当前能做的项目并从小跟堆扔到大根堆中
在大根堆中寻找当前能做的收益最大的项目
完后初始资金增加 接着判断小跟堆中能否有新的项目加入大根堆
大根堆中永远做当前收益最大的项目
这个过程一直持续到大根堆为空或已做的项目大于k
"""
import heapq


class IPO(object):
    def __init__(self, costs, profits, m, k):
        self.costs_li = costs
        self.profits_li = profits
        self.money = m
        self.project = k
        self.times = 0
        self.info_li = []
        self.canDo_li = []
        # 合并数据为一个列表 列表里包含字典
        # 其中字典的键为项目编号 值为成本和收益组成的列表
        for i in range(len(self.costs_li)):
            help_dict = {i: [costs[i], profits[i]]}
            self.info_li.append(help_dict)
        print(self.info_li)

    def ipo(self):
        # 将数据根据成本来从小到大排序 看起来好像可以不需要
        # total_list = heapq.nsmallest(len(self.costs_li), self.info_li, key=lambda s: list(s.values())[0][0])
        total_list = self.info_li
        print(total_list)
        print('')
        # 遍历项目列表 将当前成本小于资金的项目加入列表
        for i in range(len(self.costs_li)):
            if list(total_list[i].values())[0][0] <= self.money:
                self.canDo_li.append(total_list[i])
        while self.canDo_li and self.times < self.project:
            # 将当前可以投资的项目中根据收益排序最大的项目赋给当前项目
            cur_project = heapq.nlargest(1, self.canDo_li, key=lambda s: list(s.values())[0][1])
            # print(cur_project)
            # 执行当前项目并移除当前项目
            self.money += list(cur_project[0].values())[0][1]
            total_list.remove(cur_project[0])
            self.canDo_li.clear()
            for i in range(len(total_list)):
                if list(total_list[i].values())[0][0] <= self.money:
                    self.canDo_li.append(total_list[i])
            print(self.canDo_li)
        return self.money


test = IPO([100, 200, 120, 110], [10, 50, 40, 25], 115, 3)
res = test.ipo()
print('-' * 60)
print(res)
