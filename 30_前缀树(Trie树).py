"""
构建过程：
先构造一个头结点root 此时假设要把字符串'abc'加入树
那么从头结点开始 先看有'a'的路径吗(路径代表的是经过'a'而不是某个节点的值是'a')
没有的话新建一个节点 路径为'a'
然后再看'b' 之后再看'c'
到'c'的时候由于字符串已经到头了所以经过'c'路径到达的节点的值+1
此时该节点代表有一个字符串的结尾在此处
当添加其他字符串的时候 如果开始遇到相同路径了就不再建立新的路径
但分叉之后再遇到相同路径需要添加新的路径
此时要添加新功能 即得到以某一个字符串开头的字符串的个数
需要给每个节点添加一个新的数据项 即到达过该节点的次数

字典树的基本性质如下：
根节点没有字符路径。除根节点外，每一个节点都被一个字符路径找到。
从根节点到某一节点，将路径上经过的字符连接起来，为扫过的对应字符串。
每个节点向下所有的字符路径上的字符都不同。

四个主要功能：

void insert(String word)：添加word，可重复添加。
void delete(String word)：删除word，如果word添加过多次，仅删除一次。
boolean search(String word)：查询word是否在字典树中。
int prefixNumber(String pre)：返回以字符串pre为前缀的单词数量。
"""


class Node(object):
    def __init__(self):
        # 表示由多少个字符串共用这个节点
        self.path = 0
        # 表示有多少个字符串是以这个节点结尾的
        self.end = 0
        # 哈希表结构，key代表该节点的一条字符路径，value表示字符路径指向的节点
        # 此处用0-25代替26个英文字母
        self.trieNodeMap = {}
        for i in range(26):
            self.trieNodeMap[i] = None


class TrieTree(object):
    def __init__(self):
        # 建立头结点
        node = Node()
        self.root = node

    def insert(self, string):
        if not string:
            return
        new_string = str(string).lower()
        help_index_li = []
        for i in new_string:
            help_index_li.append(ord(i) - ord('a'))
        cur_node = self.root
        # print(help_index_li)
        for j in help_index_li:
            if cur_node.trieNodeMap[j] is None:
                cur_node.trieNodeMap[j] = Node()
            cur_node = cur_node.trieNodeMap[j]
            cur_node.path += 1
        cur_node.end += 1
        return "添加 '%s' 成功" % str(string)

    def delete(self, string):
        # 需要注意的是如果想删除的字符串只有一个且开始跟其他链有重合部分 那么需要处理删除过程中尾巴的问题
        if self.search(string):
            new_string = str(string).lower()
            # 默认字符串存在 等会儿添加判断逻辑
            help_index_li = []
            for i in new_string:
                help_index_li.append(ord(i) - ord('a'))
            cur_node = self.root
            for j in help_index_li:
                if cur_node.trieNodeMap[j].path == 1:
                    cur_node.trieNodeMap[j] = None
                    return "删除 '%s' 成功" % str(string)
                cur_node = cur_node.trieNodeMap[j]
                cur_node.path -= 1
            cur_node.end -= 1
            return "删除 '%s' 成功" % str(string)
        else:
            return "字符串不存在或字符串为空"

    def search(self, string):
        if not string:
            return "字符串为空"
        new_string = str(string).lower()
        help_index_li = []
        flag = False
        for i in new_string:
            help_index_li.append(ord(i) - ord('a'))
        cur_node = self.root
        for j in help_index_li:
            if cur_node.trieNodeMap[j] is None:
                return flag
            cur_node = cur_node.trieNodeMap[j]
        if cur_node.end == 1:
            flag = True
        return flag

    def prefixNumber(self, string):
        if not string:
            return "字符串为空"
        # 返回以字符串string为前缀的单词数量
        new_string = str(string).lower()
        help_index_li = []
        for i in new_string:
            help_index_li.append(ord(i) - ord('a'))
        cur_node = self.root
        help_index = 0
        while cur_node.trieNodeMap[help_index_li[help_index]] is not None:
            cur_node = cur_node.trieNodeMap[help_index_li[help_index]]
            if help_index == len(help_index_li) - 1:
                break
            help_index += 1
        return cur_node.path


if __name__ == '__main__':
    test = TrieTree()
    test.insert('abc')
    test.insert('bce')
    test.insert('abd')
    test.insert('bc')
    # print(res1, res2, res3, res4)
    # print(test.root.trieNodeMap[0].path)
    res1 = test.search('ab')
    res2 = test.search('abc')
    print(res1)
    print(res2)
    print('-' * 30)

    res3 = test.delete('ab')
    res4 = test.delete('abc')
    print(res3)
    print(res4)
    print('-' * 30)

    res5 = test.search('abc')
    print(res5)

    res6 = test.prefixNumber('bc')
    print('bc的后缀数量为:', res6)
    res6 = test.insert('bcd')
    print(res6)
    res7 = test.prefixNumber('bc')
    print('bc的后缀数量为:', res7)
    print('-' * 30)

    res8 = test.delete('bcd')
    print(res8)