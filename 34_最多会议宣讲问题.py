# 一些项目要占用一个会议室宣讲，会议室不能同时容纳两个项目
# 的宣讲。 给你每一个项目开始的时间和结束的时间(给你一个数
# 组，里面 是一个个具体的项目)，你来安排宣讲的日程，要求会
# 议室进行 的宣讲的场次最多。返回这个最多的宣讲场次。


"""
思路：
优先选择结束时间早的会议
"""
import heapq


class BestArr(object):
    def __init__(self, start, end):
        self.start_li = start
        self.end_li = end
        self.count = 0
        self.date_info = []
        self.length = len(self.start_li)
        for i in range(self.length):
            self.date_info.append({i: [self.start_li[i], self.end_li[i]]})

    def bestDate(self):
        # 将时间字符串去掉:后再转成int比较
        cur_time = '00:00'
        date_queue = heapq.nsmallest(self.length, self.date_info, key=lambda s: self.changeEndTimeToNum(s))
        print(date_queue)
        for i in range(self.length):
            if int(cur_time.replace(':', '')) <= self.changeStartTimeToNum(date_queue[i]):
                cur_time = list(date_queue[i].values())[0][1]
                self.count += 1
        return self.count

    @staticmethod
    def changeEndTimeToNum(time_str):
        return int(list(time_str.values())[0][1].replace(':', ''))

    @staticmethod
    def changeStartTimeToNum(time_str):
        return int(list(time_str.values())[0][0].replace(':', ''))


test = BestArr(['8:00', '12:20', '9:40', '18:00', '17:00', '18:00'], ['15:30', '18:00', '12:00', '20:00', '21:00', '20:00'])
res = test.bestDate()
print(res)
